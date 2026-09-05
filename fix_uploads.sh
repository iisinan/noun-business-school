#!/bin/bash
for dir in ~/Library/Application\ Support/Herd/config/php/8*; do
  if [ -d "$dir" ]; then
    echo "upload_tmp_dir=\"/tmp\"" >> "$dir/php.ini"
    echo "upload_max_filesize=\"100M\"" >> "$dir/php.ini"
    echo "post_max_size=\"100M\"" >> "$dir/php.ini"
  fi
done
echo "Fixed PHP config!"
