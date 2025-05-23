Summary:	VirtualBox - support for USB 2.0, RDP server and the PXE bootloader
Name:		VirtualBox-Extension-Pack
Version:	7.0.26
Release:	1
License:	Free for non-commercial use, non-distributable
Group:		Applications/Emulators
Source0:	http://download.virtualbox.org/virtualbox/%{version}/Oracle_VM_VirtualBox_Extension_Pack-%{version}.vbox-extpack
# Source0-md5:	9a773aa95feb62adaf1f855dc3755352
NoSource:	0
URL:		http://www.virtualbox.org/
BuildRequires:	rpmbuild(macros) >= 1.379
Requires:	VirtualBox = %{version}
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# disable debug - no symbols here
%define		_enable_debug_packages	0

%description
The Oracle VM VirtualBox Extension Pack, adds support for USB 2.0, RDP
server and the PXE bootloader with E1000 support.

%prep
%setup -qcT
%{__tar} -zxf %{SOURCE0}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/VirtualBox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack

%ifarch %{x8664}
cp -a linux.amd64 $RPM_BUILD_ROOT%{_libdir}/VirtualBox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack
%else
cp -a linux.x86 $RPM_BUILD_ROOT%{_libdir}/VirtualBox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack
%endif

install -p PXE-Intel.rom $RPM_BUILD_ROOT%{_libdir}/VirtualBox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack
install -p ExtPack.xml $RPM_BUILD_ROOT%{_libdir}/VirtualBox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/VirtualBox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack
%dir %{_libdir}/VirtualBox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.*
%attr(755,root,root) %{_libdir}/VirtualBox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.*/VBoxHostWebcam.so
%attr(755,root,root) %{_libdir}/VirtualBox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.*/VBoxNvmeR0.r0
%attr(755,root,root) %{_libdir}/VirtualBox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.*/VBoxNvmeR3.so
%attr(755,root,root) %{_libdir}/VirtualBox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.*/VBoxPuelMain.so
%attr(755,root,root) %{_libdir}/VirtualBox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.*/VBoxPuelMainVM.so
%attr(755,root,root) %{_libdir}/VirtualBox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.*/VBoxPuelCrypto.so
%attr(755,root,root) %{_libdir}/VirtualBox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.*/VBoxUsbCardReaderR3.so
%attr(755,root,root) %{_libdir}/VirtualBox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.*/VBoxUsbWebcamR3.so
%attr(755,root,root) %{_libdir}/VirtualBox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.*/VBoxVRDP.so
%attr(755,root,root) %{_libdir}/VirtualBox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.*/VDPluginCrypt.so
%{_libdir}/VirtualBox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/PXE-Intel.rom
%{_libdir}/VirtualBox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/ExtPack.xml
