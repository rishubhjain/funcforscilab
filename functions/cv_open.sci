function[img_ret]=cv_open(image)
    pyImport morphological_file
    img_ret=morphological_file.open(image)
endfunction