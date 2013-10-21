%include	/usr/lib/rpm/macros.gstreamer

%define		gstname		gst-plugins-bad
%define		gst_major_ver	1.0
%define		gst_req_ver	1.2.0

Summary:	Bad GStreamer Streaming-media framework plugins
Name:		gstreamer-plugins-bad
Version:	1.2.0
Release:	2
License:	LPL
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gst-plugins-bad/%{gstname}-%{version}.tar.xz
# Source0-md5:	4fd078e1b9d903d22b67872b616f1715
Patch0:		%{name}-musicbrainz5.patch
URL:		http://gstreamer.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	glib-devel
BuildRequires:	gstreamer-devel >= %{gst_req_ver}
BuildRequires:	gstreamer-plugins-base-devel >= %{gst_req_ver}
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	orc-devel >= 0.4.5
BuildRequires:	pkg-config
#
BuildRequires:	OpenCV-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	bzip2-devel
BuildRequires:	curl-devel
BuildRequires:	dbus-devel
BuildRequires:	faac-devel
BuildRequires:	faad2-devel
BuildRequires:	fluidsynth-devel
BuildRequires:	frei0r-devel
BuildRequires:	glib-gio-devel
BuildRequires:	gnutls-devel
BuildRequires:	jasper-devel
BuildRequires:	libass-devel >= 0.10.1-2
BuildRequires:	libcdaudio-devel
BuildRequires:	libdc1394-devel
BuildRequires:	libdca-devel
BuildRequires:	libdvdnav-devel
BuildRequires:	libdvdread-devel
BuildRequires:	libiptcdata-devel
BuildRequires:	libkate-devel
BuildRequires:	libmms-devel
BuildRequires:	libmodplug-devel
BuildRequires:	libmusicbrainz5-devel
BuildRequires:	libofa-devel
BuildRequires:	librsvg-devel
BuildRequires:	libsbc-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libusbx-devel
BuildRequires:	libwebp-devel
BuildRequires:	libx264-devel
BuildRequires:	libxml2-devel
BuildRequires:	mjpegtools-devel
BuildRequires:	mpg123-libs-devel
BuildRequires:	neon-devel
BuildRequires:	openal-soft-devel
BuildRequires:	orc-devel
BuildRequires:	rpm-gstreamerprov
BuildRequires:	rtmpdump-devel
BuildRequires:	soundtouch-devel
BuildRequires:	udev-glib-devel
BuildRequires:	vo-aacenc-devel
BuildRequires:	xorg-libX11-devel
BuildRequires:	xvidcore-devel
Requires(post,preun):	glib-gio-gsettings
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gstreamer >= %{gst_req_ver}
Requires:	gstreamer-plugins-base >= %{gst_req_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gstlibdir 	%{_libdir}/gstreamer-%{gst_major_ver}

%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plugin-based architecture means
that new data types or processing capabilities can be added simply by
installing new plugins.

%package libs
Summary:	Gstreamer bad plugins - shared libraries
Group:		Libraries

%description libs
Gstreamer base plugins - shared libraries.

%package devel
Summary:	Include files for GStreamer streaming-media framework plugins
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gstreamer-devel >= %{gst_req_ver}

%description devel
Include files for GStreamer streaming-media framework plugins.

%package apidocs
Summary:	gstreamer-plugins-bad API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gstreamer-plugins-bad API documentation.

%prep
%setup -qn %{gstname}-%{version}
#%patch0 -p1

%build
%{__autopoint}
patch -p0 < common/gettext.patch
%{__libtoolize}
%{__aclocal} -I m4 -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-gsm		\
	--disable-ladspa	\
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# We don't need plugins' *.la files
rm -f $RPM_BUILD_ROOT%{gstlibdir}/*.la

%find_lang %{gstname}-%{gst_major_ver}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_gsettings_cache

%postun
%update_gsettings_cache

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files -f %{gstname}-%{gst_major_ver}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE
%attr(755,root,root) %{gstlibdir}/libgstaccurip.so
%attr(755,root,root) %{gstlibdir}/libgstadpcmdec.so
%attr(755,root,root) %{gstlibdir}/libgstadpcmenc.so
%attr(755,root,root) %{gstlibdir}/libgstaiff.so
%attr(755,root,root) %{gstlibdir}/libgstasfmux.so
%attr(755,root,root) %{gstlibdir}/libgstassrender.so
%attr(755,root,root) %{gstlibdir}/libgstaudiofxbad.so
%attr(755,root,root) %{gstlibdir}/libgstaudiovisualizers.so
%attr(755,root,root) %{gstlibdir}/libgstautoconvert.so
%attr(755,root,root) %{gstlibdir}/libgstbayer.so
%attr(755,root,root) %{gstlibdir}/libgstbluez.so
%attr(755,root,root) %{gstlibdir}/libgstbz2.so
%attr(755,root,root) %{gstlibdir}/libgstcamerabin2.so
%attr(755,root,root) %{gstlibdir}/libgstcoloreffects.so
%attr(755,root,root) %{gstlibdir}/libgstcurl.so
%attr(755,root,root) %{gstlibdir}/libgstdashdemux.so
%attr(755,root,root) %{gstlibdir}/libgstdataurisrc.so
%attr(755,root,root) %{gstlibdir}/libgstdebugutilsbad.so
%attr(755,root,root) %{gstlibdir}/libgstdecklink.so
%attr(755,root,root) %{gstlibdir}/libgstdtsdec.so
%attr(755,root,root) %{gstlibdir}/libgstdvb.so
%attr(755,root,root) %{gstlibdir}/libgstdvbsuboverlay.so
%attr(755,root,root) %{gstlibdir}/libgstdvdspu.so
%attr(755,root,root) %{gstlibdir}/libgstfaac.so
%attr(755,root,root) %{gstlibdir}/libgstfaad.so
%attr(755,root,root) %{gstlibdir}/libgstfbdevsink.so
%attr(755,root,root) %{gstlibdir}/libgstfestival.so
%attr(755,root,root) %{gstlibdir}/libgstfieldanalysis.so
%attr(755,root,root) %{gstlibdir}/libgstfluidsynthmidi.so
%attr(755,root,root) %{gstlibdir}/libgstfragmented.so
%attr(755,root,root) %{gstlibdir}/libgstfreeverb.so
%attr(755,root,root) %{gstlibdir}/libgstfrei0r.so
%attr(755,root,root) %{gstlibdir}/libgstgaudieffects.so
%attr(755,root,root) %{gstlibdir}/libgstgdp.so
%attr(755,root,root) %{gstlibdir}/libgstgeometrictransform.so
%attr(755,root,root) %{gstlibdir}/libgstid3tag.so
%attr(755,root,root) %{gstlibdir}/libgstinter.so
%attr(755,root,root) %{gstlibdir}/libgstinterlace.so
%attr(755,root,root) %{gstlibdir}/libgstivtc.so
%attr(755,root,root) %{gstlibdir}/libgstjpegformat.so
%attr(755,root,root) %{gstlibdir}/libgstkate.so
%attr(755,root,root) %{gstlibdir}/libgstliveadder.so
%attr(755,root,root) %{gstlibdir}/libgstmfc.so
%attr(755,root,root) %{gstlibdir}/libgstmidi.so
%attr(755,root,root) %{gstlibdir}/libgstmms.so
%attr(755,root,root) %{gstlibdir}/libgstmodplug.so
%attr(755,root,root) %{gstlibdir}/libgstmpeg2enc.so
%attr(755,root,root) %{gstlibdir}/libgstmpegpsdemux.so
%attr(755,root,root) %{gstlibdir}/libgstmpegpsmux.so
%attr(755,root,root) %{gstlibdir}/libgstmpegtsdemux.so
%attr(755,root,root) %{gstlibdir}/libgstmpegtsmux.so
%attr(755,root,root) %{gstlibdir}/libgstmpg123.so
%attr(755,root,root) %{gstlibdir}/libgstmplex.so
%attr(755,root,root) %{gstlibdir}/libgstmxf.so
%attr(755,root,root) %{gstlibdir}/libgstneonhttpsrc.so
%attr(755,root,root) %{gstlibdir}/libgstofa.so
%attr(755,root,root) %{gstlibdir}/libgstopenal.so
%attr(755,root,root) %{gstlibdir}/libgstopencv.so
%attr(755,root,root) %{gstlibdir}/libgstpcapparse.so
%attr(755,root,root) %{gstlibdir}/libgstpnm.so
%attr(755,root,root) %{gstlibdir}/libgstrawparse.so
%attr(755,root,root) %{gstlibdir}/libgstremovesilence.so
%attr(755,root,root) %{gstlibdir}/libgstresindvd.so
%attr(755,root,root) %{gstlibdir}/libgstrfbsrc.so
%attr(755,root,root) %{gstlibdir}/libgstrsvg.so
%attr(755,root,root) %{gstlibdir}/libgstrtmp.so
%attr(755,root,root) %{gstlibdir}/libgstsbc.so
%attr(755,root,root) %{gstlibdir}/libgstsdpelem.so
%attr(755,root,root) %{gstlibdir}/libgstsegmentclip.so
%attr(755,root,root) %{gstlibdir}/libgstshm.so
%attr(755,root,root) %{gstlibdir}/libgstsiren.so
%attr(755,root,root) %{gstlibdir}/libgstsmooth.so
%attr(755,root,root) %{gstlibdir}/libgstsmoothstreaming.so
%attr(755,root,root) %{gstlibdir}/libgstsoundtouch.so
%attr(755,root,root) %{gstlibdir}/libgstspeed.so
%attr(755,root,root) %{gstlibdir}/libgstsubenc.so
%attr(755,root,root) %{gstlibdir}/libgstuvch264.so
%attr(755,root,root) %{gstlibdir}/libgstvideofiltersbad.so
%attr(755,root,root) %{gstlibdir}/libgstvideoparsersbad.so
%attr(755,root,root) %{gstlibdir}/libgstvoaacenc.so
%attr(755,root,root) %{gstlibdir}/libgstwebp.so
%attr(755,root,root) %{gstlibdir}/libgsty4mdec.so
%attr(755,root,root) %{gstlibdir}/libgstyadif.so
%{_datadir}/gst-plugins-bad

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_libdir}/girepository-1.0/GstInsertBin-%{gst_major_ver}.typelib
%{_libdir}/girepository-1.0/GstMpegts-%{gst_major_ver}.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/gstreamer-%{gst_major_ver}/gst/basecamerabinsrc
%{_includedir}/gstreamer-%{gst_major_ver}/gst/codecparsers
%{_includedir}/gstreamer-%{gst_major_ver}/gst/insertbin
%{_includedir}/gstreamer-%{gst_major_ver}/gst/mpegts
%{_includedir}/gstreamer-%{gst_major_ver}/gst/uridownloader
%dir %{_includedir}/gstreamer-%{gst_major_ver}/gst/interfaces
%{_includedir}/gstreamer-%{gst_major_ver}/gst/interfaces/photography-enumtypes.h
%{_includedir}/gstreamer-%{gst_major_ver}/gst/interfaces/photography.h
%{_datadir}/gir-1.0/GstInsertBin-%{gst_major_ver}.gir
%{_datadir}/gir-1.0/GstMpegts-%{gst_major_ver}.gir
%{_pkgconfigdir}/gstreamer-codecparsers-%{gst_major_ver}.pc
%{_pkgconfigdir}/gstreamer-plugins-bad-%{gst_major_ver}.pc
%{_pkgconfigdir}/gstreamer-insertbin-%{gst_major_ver}.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gst-plugins-bad-libs-*
