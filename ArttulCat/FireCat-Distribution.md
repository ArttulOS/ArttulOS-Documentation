# 🐱 ArttulCat Browser

**ArttulCat** is a lightweight, privacy-respecting Firefox fork developed by the ArttulOS team. It removes telemetry, Pocket, branding, and Mozilla experiments while offering a fast and clean experience with a custom dark interface and privacy defaults.

---

## 🚀 Features

- ✅ No telemetry, Pocket, or Mozilla Labs
- 🌑 Dark mode enabled by default
- 🏠 Homepage and new tab set to `https://xo.wtf`
- 🔍 Only one search engine: `xo.wtf` (SearX)
- 🚫 No sponsored shortcuts or suggestions
- 📦 RPM packaging for RHEL/Rocky/Fedora
- 🧼 ArttulCat branding, icon, and name throughout

---

## Repo Layout
arttulcat/
├── browser/branding/arttulcat/       # Icon & brand assets
├── browser/app/profile/firefox.js    # Custom preferences
├── browser/components/BrowserGlue.jsm
├── .mozconfig                        # Custom build config
├── README.md

## Changes I've Made
pref("browser.startup.homepage", "https://xo.wtf");
pref("browser.newtab.url", "https://xo.wtf");
pref("browser.newtabpage.enabled", false);
pref("browser.search.defaultenginename", "xo.wtf");
pref("browser.urlbar.suggest.searches", false);
pref("browser.newtabpage.activity-stream.feeds.topsites", false);
pref("browser.newtabpage.activity-stream.showSponsored", false);
pref("browser.discovery.enabled", false);
pref("browser.ping-centre.telemetry", false);
pref("toolkit.telemetry.enabled", false);
pref("extensions.getAddons.showPane", false);
pref("extensions.htmlaboutaddons.recommendations.enabled", false);


## 📦 Install Dependencies (Rocky/Fedora)

```bash
sudo dnf install clang gcc gcc-c++ make rust cargo zip unzip yasm \
autoconf213 python3-devel gtk3-devel nodejs dbus-glib-devel \
libX11-devel alsa-lib-devel libXt-devel libvpx-devel \
gstreamer1-devel gstreamer1-plugins-base-devel

## Build Instructions

git clone https://github.com/ArttulOS/arttulcat.git
cd arttulcat
./mach bootstrap
./mach build
./mach run


## RPM Packaging

cd ..
tar czf arttulcat-1.0.tar.gz arttulcat/
mv arttulcat-1.0.tar.gz ~/rpmbuild/SOURCES/

## Example Spec File
Name:           arttulcat
Version:        1.0
Release:        1%{?dist}
Summary:        ArttulCat - a privacy-respecting Firefox fork

License:        MPLv2.0
URL:            https://xo.wtf
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cargo clang gcc gcc-c++ make python3-devel zip unzip yasm
BuildRequires:  libX11-devel libXt-devel libvpx-devel dbus-glib-devel alsa-lib-devel
BuildRequires:  gtk3-devel glib2-devel gstreamer1-devel gstreamer1-plugins-base-devel
BuildRequires:  nodejs python3-setuptools rust rust-std-static
BuildRequires:  autoconf213

Requires:       gtk3, libX11

%description
ArttulCat is a lightweight, debranded Firefox fork built for privacy and minimalism.

%prep
%autosetup

%build
export MOZBUILD_STATE_PATH=%{_builddir}/.mozbuild
./mach build

%install
mkdir -p %{buildroot}/opt/%{name}
./mach install --prefix=%{buildroot}/opt/%{name}
mkdir -p %{buildroot}/usr/bin
ln -s /opt/%{name}/bin/firefox %{buildroot}/usr/bin/arttulcat

%files
%license LICENSE
%doc README.md
/opt/%{name}
/usr/bin/arttulcat

%changelog
* Sat May 03 2025 ArttulOS Team <dev@xo.wtf> - 1.0-1
- Initial RPM package of ArttulCat

## Build the RPM
cd ~/rpmbuild/SPECS
rpmbuild -ba arttulcat.spec

## Install the RPM/Output Directory
sudo dnf install ~/rpmbuild/RPMS/x86_64/arttulcat-1.0-1.el9.x86_64.rpm



---

✅ You can now **copy and paste the entire block above** into your `README.md`, website, GitHub page, or any documentation file.

Would you like me to generate a pre-filled `.tar.gz` or `.rpm` manifest structure as well?
