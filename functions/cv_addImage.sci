function[img_ret]=cv_addimage(image,image1)
    pyImport addimage
    img_ret=addimage.add(image,image1)
endfunction
