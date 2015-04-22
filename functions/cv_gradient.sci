
function[img_ret]=cv_gradient(image)
    pyImport morphological_file
    img_ret=morphological_file.dilate(image)
endfunction
