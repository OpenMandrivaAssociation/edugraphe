Name:           edugraphe
Version:        1.1
Release:        3
Summary:        Plotting program in Java

Group:          Sciences/Other
License:        GPL
URL:            http://joel.amblard.pagesperso-orange.fr
Source0:        http://joel.amblard.pagesperso-orange.fr/prg/edu/edugraphe-1.1.zip
Source1:       %{name}.desktop
Source2:       %{name}.gif
Source3:       %{name}.sh
BuildArch:      noarch


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
# install jar
mkdir -p %{buildroot}%{_javadir}
cp -p source/classes/edugraphe.jar   \
%{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# install javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp source/images  \
%{buildroot}%{_javadocdir}/%{name}
cp -p source/manuel.html  \
%{buildroot}%{_javadocdir}/%{name}
cp -p source/manuel_fr.html  \
%{buildroot}%{_javadocdir}/%{name}

# install demo
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -p *.txt \
%{buildroot}%{_datadir}/%{name}
cp -rp demo  \
%{buildroot}%{_datadir}/%{name}/demo

# install icon
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp -p %{SOURCE2} %{buildroot}%{_datadir}/pixmaps

# install script
mkdir -p %{buildroot}%{_bindir}
chmod +x %{SOURCE3}
cp -p  %{SOURCE3} %{buildroot}%{_bindir}/%{name}


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


%files
%defattr(-,root,root,-)
%{_javadir}/*
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/edugraphe.gif
%{_datadir}/javadoc/*
%{_bindir}/%{name}




%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.1-2mdv2011.0
+ Revision: 675856
- clean desktop file

* Mon Mar 07 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 642397
- Import edugraphe 1.1
  CCBUG: 62716
- edugraphe 1.1

