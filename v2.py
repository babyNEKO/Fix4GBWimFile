from rich import print
from sys import platform
from os.path import exists
from os import system, remove


class FixWimFile:
    u_disk = ''
    iso_disk = ''

    def __init__(self):
        self.DISK = ['D', 'E', 'F', 'J', 'H', 'I', 'G', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
                     'X', 'Y', 'Z']
        self.DISM_CMD = 'dism /Split-Image /ImageFile:{iso_disk}:\sources\install.wim /SWMFile:{u_disk}:\sources\install.swm /FileSize:3800'
        self.U_PATH = '{}:\sources\install.wim'
        self.README = '''
    [bold blue]Version 1.2.5, Build-14, Stable.[/bold blue]
    Power By [bold green]mr_bug@foxmail.com[/bold green]
    -----------------------------------
    Fat32不支持大于4G文件，使用此工具进行wim文件分割。使用系统自带工具DISM
    [bold red]
    [提示信息]
        ※ 操作系统Windows 10
        ※ 请使用管理员权限运行此程序
        ※ 开始之前请提前挂载好ISO文件到虚拟光驱[/bold red]\n'''

    def check_wim_exists(self):
        if input('\n删除U盘中的install.wim 此操作不可逆 输入Y确认删除[N]：').upper() == str('Y'):
            if exists(self.U_PATH.format(FixWimFile.u_disk)):
                print('[bold red]删除[/bold red] install.wim')
                remove(self.U_PATH.format(FixWimFile.u_disk))
                print('[bold green]已删除[/bold green]')
        else:
            print('操作取消')
            exit(0)

    def fix_wim(self):
        print('\n[bold green]请稍等，正在执行文件分割... ...[/bold green]')
        system(self.DISM_CMD.format(iso_disk=FixWimFile.iso_disk, u_disk=self.U_PATH.format(FixWimFile.u_disk)))
        system('pause')

    def run(self):
        try:
            system('chcp 65001')
            assert ('win' in platform), 'only windows platform'.title()
            print(self.README)
            u = input('输入U盘盘符：')
            if u.upper() in self.DISK:
                FixWimFile.u_disk = u.upper()
            iso = input('输入虚拟光驱盘符：')
            if iso.upper() in self.DISK:
                FixWimFile.iso_disk = iso.upper()

            self.check_wim_exists()
            self.fix_wim()

        except AssertionError as AE:
            print(AE)
        except KeyboardInterrupt as KI:
            print(KI)


if __name__ == '__main__':
    FixWimFile().run()
