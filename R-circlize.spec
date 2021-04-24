#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-circlize
Version  : 0.4.12
Release  : 37
URL      : https://cran.r-project.org/src/contrib/circlize_0.4.12.tar.gz
Source0  : https://cran.r-project.org/src/contrib/circlize_0.4.12.tar.gz
Summary  : Circular Visualization
Group    : Development/Tools
License  : MIT
Requires: R-GlobalOptions
Requires: R-colorspace
Requires: R-shape
BuildRequires : R-GlobalOptions
BuildRequires : R-colorspace
BuildRequires : R-shape
BuildRequires : buildreq-R

%description
amounts of information. Here this package provides an implementation 
    of circular layout generation in R as well as an enhancement of available 
    software. The flexibility of the package is based on the usage of low-level 
    graphics functions such that self-defined high-level graphics can be easily 
    implemented by users for specific purposes. Together with the seamless 
    connection between the powerful computational and visual environment in R, 
    it gives users more convenience and freedom to design figures for 
    better understanding complex patterns behind multiple dimensional data.

%prep
%setup -q -c -n circlize
cd %{_builddir}/circlize

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610121209

%install
export SOURCE_DATE_EPOCH=1610121209
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library circlize
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library circlize
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library circlize
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc circlize || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/circlize/CITATION
/usr/lib64/R/library/circlize/DESCRIPTION
/usr/lib64/R/library/circlize/INDEX
/usr/lib64/R/library/circlize/LICENSE
/usr/lib64/R/library/circlize/Meta/Rd.rds
/usr/lib64/R/library/circlize/Meta/demo.rds
/usr/lib64/R/library/circlize/Meta/features.rds
/usr/lib64/R/library/circlize/Meta/hsearch.rds
/usr/lib64/R/library/circlize/Meta/links.rds
/usr/lib64/R/library/circlize/Meta/nsInfo.rds
/usr/lib64/R/library/circlize/Meta/package.rds
/usr/lib64/R/library/circlize/Meta/vignette.rds
/usr/lib64/R/library/circlize/NAMESPACE
/usr/lib64/R/library/circlize/NEWS
/usr/lib64/R/library/circlize/R/circlize
/usr/lib64/R/library/circlize/R/circlize.rdb
/usr/lib64/R/library/circlize/R/circlize.rdx
/usr/lib64/R/library/circlize/demo/foo.R
/usr/lib64/R/library/circlize/doc/circlize.Rmd
/usr/lib64/R/library/circlize/doc/circlize.html
/usr/lib64/R/library/circlize/doc/index.html
/usr/lib64/R/library/circlize/extdata/DMR.RData
/usr/lib64/R/library/circlize/extdata/Rlogo.png
/usr/lib64/R/library/circlize/extdata/bird.orders.RData
/usr/lib64/R/library/circlize/extdata/chromInfo.txt
/usr/lib64/R/library/circlize/extdata/chrom_info_list.rds
/usr/lib64/R/library/circlize/extdata/cytoBand.txt
/usr/lib64/R/library/circlize/extdata/cytoband_list.rds
/usr/lib64/R/library/circlize/extdata/doodle.RData
/usr/lib64/R/library/circlize/extdata/download_and_slice_doodle.R
/usr/lib64/R/library/circlize/extdata/download_ucsc.R
/usr/lib64/R/library/circlize/extdata/tagments_WGBS_DMR.RData
/usr/lib64/R/library/circlize/extdata/tp_family.RData
/usr/lib64/R/library/circlize/extdata/tp_family_df.rds
/usr/lib64/R/library/circlize/help/AnIndex
/usr/lib64/R/library/circlize/help/aliases.rds
/usr/lib64/R/library/circlize/help/circlize.rdb
/usr/lib64/R/library/circlize/help/circlize.rdx
/usr/lib64/R/library/circlize/help/paths.rds
/usr/lib64/R/library/circlize/html/00Index.html
/usr/lib64/R/library/circlize/html/R.css
