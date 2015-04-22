function[img_ret]=cv_tophat(image)
    pyImport morphological_file
    img_ret=morphological_file.dilate(image)
endfunction