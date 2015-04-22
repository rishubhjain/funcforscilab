function[img_ret]=cv_blackhat(image)
    pyImport morphological_file
    img_ret=morphological_file.dilate(image)
endfunction