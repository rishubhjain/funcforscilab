function[img_ret]=cv_erode_path(path,iterations)
    pyImport morphological_file
    img_ret=morphological_file.erode_path(path,iterations)
endfunction
