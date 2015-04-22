function [img_ret]= cv_cornerHarris_path(path)
    pyImport cornerHarris_file
    image_ret=cornerHarris_file.cornerHarris_path(path)
endfunction
