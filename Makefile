all:
	meson bin --prefix /dev_ws/src/gd_control/gd_control
	cd bin; meson configure -D python=true
	cd bin; ninja

install:
	cd bin; ninja install
	cd overlays; sh overlay.sh

clean:
	rm -rf bin
	rm -f overlays/*.dtbo
