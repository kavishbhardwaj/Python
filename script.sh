mkdir -p project/directory1 project/directory2
touch project/directory1/file1.txt project/directory1/file2.txt
touch project/directory2/file3.txt project/directory2/file4.txt
touch project/original_file.txt
ln project/directory1/file1.txt project/hardlink_to_file1.txt
ln -s project/directory1/file2.txt project/softlink_to_file2.txt
