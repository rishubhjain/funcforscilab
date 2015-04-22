function[image_ret]=cv_putText(img,text,org1,color1)
    pyImport drawing_file
    image_ret=drawing_file.myputText(img,text,org1,color1)
endfunction
