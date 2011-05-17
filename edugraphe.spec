Name:           edugraphe
Version:        1.1
Release:        %mkrel 2
Summary:        edugraphe is a plotting program in Java

Group:          Sciences/Other
License:        GPL
URL:            http://joel.amblard.pagesperso-orange.fr
Source0:        http://joel.amblard.pagesperso-orange.fr/prg/edu/edugraphe-1.1.zip
Source1:       %{name}.desktop
Source2:       %{name}.gif
Source3:       %{name}.sh
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}


BuildRequires:  jpackage-utils
BuildRequires:  java-devel
BuildRequires:  desktop-file-utils


Requires:       jpackage-utils
Requires:       java-1.6.0-devel

%description
edugraphe is a plotting program in Java


%prep
%setup -q -n "%{name}-%{version}" 
# erase object and useless files 
rm %{name}.jar
cd source/classes
find -name '*.class' -exec rm -f '{}' \;
cd ../..


%build
cd source
/bin/sh compile.sh
cd ..

%install
rm -rf $RPM_BUILD_ROOT
# install jar
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p source/classes/edugraphe.jar   \
$RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# install javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp source/images  \
$RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -p source/manuel.html  \
$RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -p source/manuel_fr.html  \
$RPM_BUILD_ROOT%{_javadocdir}/%{name}

# install demo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -p *.txt \
$RPM_BUILD_ROOT%{_datadir}/%{name}
cp -rp demo  \
$RPM_BUILD_ROOT%{_datadir}/%{name}/demo

# install icon
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps

# install script
mkdir -p $RPM_BUILD_ROOT%{_bindir}
chmod +x %{SOURCE3}
cp -p  %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/%{name}


# desktop file
desktop-file-install --vendor=""                     \
       --dir=%{buildroot}%{_datadir}/applications/   \
       %{SOURCE1}

%post
#update icon cache
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache -q %{_datadir}/icons/hicolor;
fi
update-desktop-database &> /dev/null || :

%postun
# update icon cache
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache -q %{_datadir}/icons/hicolor;
fi
update-desktop-database &> /dev/null || :


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_javadir}/*
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/edugraphe.gif
%{_datadir}/javadoc/*
%{_bindir}/%{name}


