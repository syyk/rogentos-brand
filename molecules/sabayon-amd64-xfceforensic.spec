# Use abs path, otherwise daily builds automagic won't work
%env %import ${ROGENTOS_MOLECULE_HOME:-/sabayon}/molecules/forensicxfce.common

# Release Version
release_version: 9

# Release Version string description
release_desc: amd64 ForensicsXfce

# Path to source ISO file (MANDATORY)
%env source_iso: ${ROGENTOS_MOLECULE_HOME:-/sabayon}/iso/Sabayon_Linux_DAILY_amd64_Xfce.iso

destination_iso_image_name: Sabayon_Linux_DAILY_amd64_ForensicsXfce.iso
