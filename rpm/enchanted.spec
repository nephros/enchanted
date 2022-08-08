Name:          enchanted-sound-theme
Version:       1.1
Release:       1
License:       GPLv3
Group:         Unspecified
Summary:       Enchanted sound theme
URL:           https://github.com/rtlewis88/rtl88-Themes/tree/Enchanted-Complete-System-Sounds
#Icon: pic.png
BuildArch:     noarch

%define themename Enchanted
%define themedir %{_datadir}/sounds/%{themename}
%define stereodir %{themedir}/stereo

%description
Set of tones compiled from the 'Enchanted' desktop sound theme by rtl88.

Original description:

Enchanted-Complete-System-Sounds will fill your computer with added life, but
only in a way that improves the experience - versus overwhelming it.
You will immediately be transformed into a universe where pleasant and
reassuring conformations follow you everywhere you travel.

%prep

%install

%build

%files
%doc README.md
%dir % "%{_datadir}/sounds/%{themename}"
%dir %{themedir}
"%{themedir}/index.theme"
"%{themedir}/stereo.index"
"%{stereodir}/*.ogg"

%post -p /bin/sh
if [ $1 -eq 1 ] ; then 
        # Initial installation 
        systemctl --no-reload preset --user --global restart ambienced >/dev/null 2>&1 || : 
fi 

%changelog

