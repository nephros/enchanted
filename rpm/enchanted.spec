Name:          enchanted-sound-theme
Version:       1.1
Release:       1
License:       Creative Commons Attribution ShareAlike
Group:         Unspecified
Summary:       Enchanted sound theme
URL:           https://github.com/rtlewis88/rtl88-Themes/tree/Enchanted-Complete-System-Sounds
Source0:       %{name}-%{version}.tar.gz
Source1:       stereo.index
BuildArch:     noarch

%define themename Enchanted
%define themedir %{_datadir}/sounds/%{themename}
%define stereodir %{themedir}/stereo

%description
Set of tones compiled from the 'Enchanted' desktop sound theme by Randall Lewis (rtl88)

Original description:

Enchanted-Complete-System-Sounds will fill your computer with added life, but
only in a way that improves the experience - versus overwhelming it.  You will
immediately be transformed into a universe where pleasant and reassuring
conformations follow you everywhere you travel.

%if "%{?vendor}" == "chum"
PackageName: Enchanted sound theme
PackageName: nephros
PackagerName: nephros
DeveloperName: Randall Lewis
DeveloperLogin: rtl88
Type: addon
Categories:
  - Graphics
  - Settings
Icon: https://raw.githubusercontent.com/rtlewis88/rtl88-Themes/Enchanted-Complete-System-Sounds/Pic.png
Url:
  Homepage: https://store.kde.org/p/1332121
%endif

%prep
%setup -q -n %{name}-%{version}/upstream

%install
install -D -m 644 %{themename}/index.theme %{buildroot}%{themedir}/index.theme
install -D -m 644 %{SOURCE1} %{buildroot}%{themedir}/stereo.index
pushd %{themename}/stereo/
for f in *.ogg
do
    install -D -m 644 $f %{buildroot}%{stereodir}/$f
done
popd

%build

%files
%doc README.md
%defattr(-,root,root,-)
%dir %{themedir}
%%{themedir}/index.theme
%%{themedir}/stereo.index
%dir %{stereodir}
#%%{stereodir}/*.ogg
# less usable files shall not be packaged
%exclude %{stereodir}/audio-volume-change.ogg
%exclude %{stereodir}/button-pressed.ogg
%exclude %{stereodir}/button-released.ogg
%exclude %{stereodir}/dialog-information.ogg
%exclude %{stereodir}/menu-replace.ogg
%exclude %{stereodir}/window-maximized.ogg
%exclude %{stereodir}/window-slide.ogg
%exclude %{stereodir}/window-switch.ogg
%exclude %{stereodir}/window-unmaximized.ogg


%postun -p /bin/sh
    systemctl --no-reload preset --user --global restart ambienced >/dev/null 2>&1 || : 


%post -p /bin/sh
if [ $1 -eq 1 ] ; then 
        # Initial installation 
        systemctl --no-reload preset --user --global restart ambienced >/dev/null 2>&1 || : 
fi 

%changelog

