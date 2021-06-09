from playwright import sync_playwright
import time
from tqdm import tqdm
def get_repositories(url):
    import os
    import shutil
    path = os.getcwd()+r'\MinGit-2.30.0.2-64-bit\cmd\git.exe'    #获取"bin"文件夹位置
    os.system('%s init'%(path))    #初始化git
    os.system('%s config --system http.sslverify false'%(path))
    os.system('%s clone %s'%(path,url))    #用clone功能下载库
    shutil.rmtree(".git")    #删除".git"文件夹，以免造成错误
    print("下载完成")
def run(playwright):
    global url
    global x
    global y
    z = input('\ngithub仓库链接（最后不带斜杠）：')
    browser = playwright.chromium.launch(headless=True)
    context = browser.newContext()

    # Open new page
    page = context.newPage()

    # Go to https://gitee.com/
    page.goto("https://gitee.com/")

    # Click div[id="git-nav-user-bar"] >> text=/.*登录.*/
    page.click("div[id=\"git-nav-user-bar\"] >> text=/.*登录.*/")
    # assert page.url == "https://gitee.com/login"

    # Click input[name="user[login]"]
    page.click("input[name=\"user[login]\"]")

    # Fill input[name="user[login]"]
    page.fill("input[name=\"user[login]\"]", x)

    # Fill input[name="user[password]"]
    page.fill("input[name=\"user[password]\"]", y)

    page.click("input[name=\"commit\"]")

    # Click //div[normalize-space(.)='新建仓库 发布代码片段 创建组织 开通企业版 从 GitHub / GitLab 导入仓库']/i
    page.click("//div[normalize-space(.)='新建仓库 发布代码片段 创建组织 开通企业版 从 GitHub / GitLab 导入仓库']/i")

    # Click text=/.*从 GitHub / GitLab 导入仓库.*/
    page.click("text=/.*从 GitHub / GitLab 导入仓库.*/")
    # assert page.url == "https://gitee.com/projects/import/url"

    # Click input[name="project[import_url]"]
    page.click("input[name=\"project[import_url]\"]")

    # Fill input[name="project[import_url]"]
    page.fill("input[name=\"project[import_url]\"]", z)

    # Click text="公开"
    page.click("text=\"公开\"")

    # Click input[name="commit"]
    page.click("input[name=\"commit\"]")

    url = 'https://gitee.com/%s/%s'%(x,z.split('/')[-1])

    for i in tqdm(range(31),ncols=75,desc='进行中'):
        time.sleep(1)
    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()
def main():
    with sync_playwright() as playwright:
        run(playwright)
    get_repositories(url)
if __name__ == '__main__':
    x = input('gitee用户名（不要电话,按q退出）：')
    y = input('\ngitee密码：')
    while x != 'q' or x != 'Q':
        main()



