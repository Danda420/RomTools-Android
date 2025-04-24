# CLI ROM Tools for Android
## Android Kitchen written in bash
### Setup ###
- Download this repository code as zip
- Extract the RomTools folder inside to any dirs in /data
- Execute the start script inside that extracted folder via terminal (ofc with su) then choose install tool option
- After installation is complete, you can just do su -c romtools on terminal to start the tool
***
### Features ###
- Unpack and repack super, ext4, erofs.
- Converting images
  - sparse to raw & raw to sparse
  - erofs to ext4, ext4 to erofs
  - raw to dat.br & dat.br to raw
  - and so on...
- Auto generate missing fs_config (file perms depends on the location)
- Mount and umount images
- Custom Scripts (put your scripts into tool/custom_scripts, you can use functions from tool)
- Zstd unpacking and repacking

| Supported Image Types                   |
|-----------------------------------------|
| Super                                   |
| Ext4                                    |
| Erofs                                   |
| Payload (unpack)                        |
| Sparsechunk (decompress)                |
***

### Credits ###

[xpirt-sdat2img](https://github.com/xpirt/sdat2img)

[xpirt-img2sdat](https://github.com/xpirt/img2sdat)

[althafvly-imgextractor](https://github.com/althafvly/AmlogicKitchen/blob/master/bin/imgextractor.py)

