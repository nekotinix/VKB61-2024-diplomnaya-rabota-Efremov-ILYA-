import pyfstool
image_path = 'virtual_disk.img'
disk_size = 1024 * 1024 * 100  # 100 MB
filesystem_type = 'ext4'
handler = pyfstool.VDIHandler(image_path)
handler.create(disk_size, filesystem_type)
mount_path = '/mnt/virtual_disk'
handler.mount(mount_path)
file_path = '/mnt/virtual_disk/test.txt'
with open(file_path, 'w') as f:
    f.write('Hello, virtual disk!')
with open(file_path, 'r') as f:
    content = f.read()
    print(content)    
	
handler.unmount(mount_path)    