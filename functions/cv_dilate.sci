function[img_ret]=cv_dilate(image,iterations)
    pyImport morphological_file
    img_ret=morphological_file.dilate(image,iterations)
endfunction