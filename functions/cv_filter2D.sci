function[img_ret]=cv_filter2D(image,ddepth)
    pyImport filter2D
    imag_ret=filter2D.filter2D(image,ddepth)
endfunction