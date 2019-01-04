subarch: amd64
version_stamp: petrichor.2018.12
target: livecd-stage1
rel_type: default
profile: default/linux/amd64/17.0
snapshot: petrichor.2018.12
source_subpath: default/stage3-amd64-20181223T214502Z
compression_mode: pixz_x

livecd/use:
	fbcon
	ipv6
	livecd
	lvm1
	modules
	ncurses
	nls
	nptl
        pam
	python
	readline
	socks5
	ssl
	static-libs
	unicode
	xml
        -static

livecd/packages:
	app-accessibility/brltty
	app-admin/hddtemp
	app-admin/passook
	app-admin/pwgen
	app-admin/syslog-ng
	app-arch/unzip
	app-crypt/gnupg
	app-editors/mg
	app-editors/nano
	app-misc/screen
	app-portage/mirrorselect
	app-text/wgetpaste
	media-gfx/fbgrab
	net-analyzer/traceroute
	net-dialup/mingetty
	net-dialup/pptpclient
	net-dialup/rp-pppoe
	net-fs/cifs-utils
	net-fs/nfs-utils
	net-irc/irssi
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/ndisc6
	net-misc/ntp
	net-misc/openssh
	net-misc/rdate
	net-misc/rsync
	net-misc/vconfig
	net-proxy/dante
	net-proxy/tsocks
	net-wireless/b43-fwcutter
### Masked (~keywords)
#	net-wireless/bcm43xx-fwcutter
	net-wireless/iw
	net-wireless/wireless-tools
	net-wireless/wpa_supplicant
	sys-apps/busybox
	sys-apps/dmidecode
	sys-apps/ethtool
	sys-apps/fxload
	sys-apps/gptfdisk
	sys-apps/hdparm
	sys-apps/hwsetup
	sys-apps/iproute2
	sys-apps/memtester
	sys-apps/netplug
	sys-apps/pciutils
	sys-apps/sdparm
	sys-apps/usbutils
	sys-block/parted
	sys-block/partimage
	sys-firmware/ipw2100-firmware
	sys-firmware/ipw2200-firmware
	sys-fs/btrfs-progs
	sys-fs/cryptsetup
	sys-fs/dmraid
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/f2fs-tools
	sys-fs/jfsutils
	sys-fs/lsscsi
	sys-fs/lvm2
	sys-fs/mac-fdisk
	sys-fs/mdadm
	sys-fs/multipath-tools
	sys-fs/ntfs3g
	sys-fs/reiserfsprogs
	sys-fs/xfsprogs
	#force rebuild for USE="(-multilib*)"
	sys-libs/glibc
	sys-libs/gpm
	sys-power/acpid
	www-client/links
