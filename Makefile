# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
LANG            = es_ES
# currently we are building for the following languages, if you want yours to be build: ask!
LANGUAGES       = en es_ES ca_ES
SPHINXOPTS      =
# Use the tag i18n to filter text based on whether we are translating or not
SPHINXINTLOPTS  = $(SPHINXOPTS) -D language=$(LANG) -t i18n
SPHINXBUILD     ?= sphinx-build
SPHINXINTL      ?= sphinx-intl
SOURCEDIR       = .
BUILDDIR        = build
# to be able to run the Makefile in a docker you have to mount (with -v) your site dir on /site
SITEDIR         = ./site
VERSION         = testing

# needed for Sphinx > 4.5?
export LC_ALL=C.UTF-8

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

html:
	echo "$(SPHINXOPTS) $(SPHINXINTLOPTS)"
	if [ $(LANG) != "en" ]; then \
		$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)/html/$(LANG)" $(SPHINXINTLOPTS) $(0); \
	else \
		$(SPHINXBUILD) -b html -nW --keep-going "$(SOURCEDIR)" "$(BUILDDIR)/html/$(LANG)" $(SPHINXOPTS) $(0); \
	fi

zip:
	mkdir -p $(BUILDDIR)/zip;
	(cd $(BUILDDIR)/html; \
	zip -r Giswater-$(VERSION)-Documentation-$(LANG).zip $(LANG)/;)
	mv $(BUILDDIR)/html/Giswater-$(VERSION)-Documentation-$(LANG).zip $(BUILDDIR)/zip/;

site: html zip
	rsync -hvrzc --delete --progress $(BUILDDIR)/html/$(LANG) $(SITEDIR)/;

full: html zip
	make LANG=$(LANG) pdf;