%define rbname xpath

Summary:	Generate XPath expressions from Ruby
Name:		rubygem-%{rbname}
Version:	2.0.0
Release:	1
License:	GPLv2+ or Ruby
Group:		Development/Ruby
Url:		https://rubygems.org/gems/%{rbname}
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems
BuildArch:	noarch

%description
XPath is a Ruby DSL for generating XPath expressions.

%files
%dir %{gem_dir}/gems/%{rbname}-%{version}
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib
%{gem_dir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/xpath
%{gem_dir}/gems/%{rbname}-%{version}/lib/xpath/*.rb
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec

#----------------------------------------------------------------------------

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{EVRD}

%description doc
Documents, RDoc & RI documentation for %{name}.

%files doc
%{gem_dir}/doc/%{rbname}-%{version}
%{gem_dir}/gems/%{rbname}-%{version}/README.md

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%gem_build

%install
%gem_install

