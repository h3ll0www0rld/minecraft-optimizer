import yaml
import json
import requests 
import questionary
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

class UnCompatibleError(Exception):
    def __init__(self, message):
        self.message = message

def getDownloadUrl(modID:str,mcVersion: str,loader:str) -> str:
    _response = json.loads(requests.get(f"https://api.modrinth.com/v2/project/{modID}/version").text)
    for version in _response:
        if mcVersion in version["game_versions"] and loader in version["loaders"]:
            return version["files"][0]["url"]
    raise UnCompatibleError(f"{modID}不兼容版本{mcVersion}!")

def downloadFile(url, folder):
    localFilename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        total_size = int(r.headers.get('content-length', 0))
        with open(os.path.join(folder, localFilename), 'wb') as f, tqdm(
            desc=localFilename,
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for data in r.iter_content(chunk_size=1024):
                size = f.write(data)
                bar.update(size)
    return localFilename

def main():
    versionIsolation = questionary.select("版本隔离",choices=["已开启","未开启"]).ask()

    mcVersion = questionary.select("请选择你的MC版本",choices=os.listdir(".minecraft/versions")).ask()

    modsFolder = ".minecraft/versions/mods" if versionIsolation == "已开启" else ".minecraft/mods"
    with open ("ModList.yaml","r") as f:
        config = yaml.safe_load(f)
    
    loader = config["loader"]
    mods = config["mods"]
    
    downloadList = []
    successCount = 0
    for modID in mods:
        print(f"正在获取{modID}的下载链接......")
        try:
            downloadList.append(getDownloadUrl(modID,mcVersion,loader))
            print("获取成功")
            successCount += 1
        except UnCompatibleError as e:
            print(e)
    print(f"成功获取{successCount}个模组的下载地址，共{len(mods)}个模组")
    with ThreadPoolExecutor(max_workers=4) as executor:
        futureToUrl = {executor.submit(downloadFile, url, modsFolder): url for url in downloadList}
        for future in as_completed(futureToUrl):
            url = futureToUrl[future]
            try:
                result = future.result()
            except Exception as exc:
                print(f"下载{url}时错误: {exc}")

if __name__ == "__main__":
    main()
