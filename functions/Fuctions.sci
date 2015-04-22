pyAddToPath("N:\project\Python_Files\")
pyImport imp
//imp.reload("N:\project\Python_Files\")

//image burring is left..no documentation
//open closse function->kya hain pata nai...give proper function name   

function [image] = cv_rgb2gray_path(path)  
    
    pyImport rgb2gray_file
    image=rgb2gray_file.rgb2gray(path)

endfunction 


function[img_ret]=cv_imshow(image)
    pyImport imshow
    img_ret=imshow.imshow1(image)
endfunction

function[image]=cv_imread(image_path)
    pyImport imread1
    image=imread1.imread(image_path)
endfunction

function [image_ret]=cv_rgb2gray_image(image)
    image_ret=rgb2gray(image)

endfunction

//please dont use this for now
function [img_ret]= cv_cornerHarris_path(path)
    pyImport cornerHarris_file
    image_ret=cornerHarris_file.cornerHarris_path(path)
endfunction

function [img_ret]= cv_cornerHarris_image(image,blocksize,ksize,k)
    pyImport cornerHarris_file
    img_ret=cornerHarris_file.cornerHarris_image(image,blocksize,ksize,k)
endfunction

function [img_ret]=cv_pyrDown_path(path)
    pyImport pyr_file
    img_ret=pyr_file.pyrDown_path(path)
endfunction

function [img_ret]=cv_pyrDown_image(image)
    pyImport pyr_file
    img_ret=pyr_file.pyrDown_path(image)
endfunction

function [img_ret]=cv_pyrUp_path(path)
    pyImport pyr_file
    img_ret=pyr_file.pyrUp_path(path)
endfunction

function [img_ret]=cv_pyrUp_image(image)
    pyImport pyr_file
    img_ret=pyr_file.pyrUp_image(image)
endfunction

function [img_ret]=cv_equalizeHist_path(path)
    pyImport equalizeHist_file
    img_ret=equalizeHist_file.equalizeHist_path(path)
endfunction

function [img_ret]=cv_equalizeHist_image(image)
    pyImport equalizeHist_file
    img_ret=equalizeHist_file.equalizeHist_image(image)
endfunction
//what is X in this?

function [img_ret]=cv_warpAffine_path(path)
    pyImport warpAffine_file
    img_ret=warpAffine_file.warpAffine_path(path)
endfunction

function [img_ret]=cv_warpAffine_image(image)
    pyImport warpAffine_file
    img_ret=warpAffine_file.warpAffine_image(image)
endfunction
//erode...will have to work on kernal
function[img_ret]=cv_erode_path(path,iterations)
    pyImport morphological_file
    img_ret=morphological_file.erode_path(path,iterations)
endfunction

function[img_ret]=cv_erode_image(image,iterations)
    pyImport morphological_file
    img_ret=morphological_file.erode_image(image,iterations)
endfunction


function[img_ret]=cv_dilate(image,iterations)
    pyImport morphological_file
    img_ret=morphological_file.dilate(image,iterations)
endfunction


function[img_ret]=cv_open(image)
    pyImport morphological_file
    img_ret=morphological_file.open(image)
endfunction

function[img_ret]=cv_close(image)
    pyImport morphological_file
    img_ret=morphological_file.close(image)
endfunction

function[img_ret]=cv_gradient(image)
    pyImport morphological_file
    img_ret=morphological_file.dilate(image)
endfunction

function[img_ret]=cv_tophat(image)
    pyImport morphological_file
    img_ret=morphological_file.dilate(image)
endfunction

function[img_ret]=cv_blackhat(image)
    pyImport morphological_file
    img_ret=morphological_file.dilate(image)
endfunction

function[image_ret]=cv_Line(image,start,end1,color1)
    pyImport drawing_file
    //omitted parameters like thickness, lineType, shift
    image_ret=drawing_file.myLine(image,start,end1,color1)
endfunction

//function[]=cv_Line(image,start,end)
   // pyImport drawing_file
  //  drawing_file.myLine(image,start,end)
//endfunction

function[image_ret]=cv_Rect(image,start,end1,color1)
    pyImport drawing_file
    image_ret=drawing_file.myRect(image,start,end1,color1)
endfunction

function[image_ret]=cv_Circle(img,center1,radius,color1)
    pyImport drawing_file
    image_ret=drawing_file.myCircle(img,center1,radius,color1)
endfunction

function[image_ret]=cv_Ellipse(img,cent, axes1, angle, startAngle, endAngle,color1)
    pyImport drawing_file
    image_ret=drawing_file.myLine(img,cent, axes1, angle, startAngle, endAngle,color1)
endfunction

function[image_ret]=cv_putText(img,text,org1,color1)
    pyImport drawing_file
    image_ret=drawing_file.myputText(img,text,org1,color1)
endfunction

function[img_ret]=cv_addimage(image,image1)
    pyImport addimage
    img_ret=addimage.add(image,image1)
endfunction

function[img_ret]=cv_threshold_mean(image,maxValue)
    pyImport adaptive_threshold
    img_ret=adaptive_threshold.adaptive_thresh_mean(image,maxValue)
endfunction

function[img_ret]=cv_threshold_gaussian(image,maxValue)
    pyImport adaptive_threshold
    img_ret=adaptive_threshold.adaptive_thresh_gaussian(image,maxValue)
endfunction

//kernal not taken as parameter
function[img_ret]=cv_filter2D(image,ddepth)
    pyImport filter2D
    imag_ret=filter2D.filter2D(image,ddepth)
endfunction

function[img_ret]=cv_otus_binarization(image)
    pyImport Otus_binarization
    img_ret=Otus_binarization.otus(image)
endfunction

function[img_ret]=cv_thresh_binary(image)
    pyImport simple_thresholding
    img_ret=simple_thresholding.thresh_binary(image)
endfunction

function[img_ret]=cv_thresh_binary_inverse(image)
    pyImport simple_thresholding
    img_ret=simple_thresholding.thresh_binary_inv(image)
endfunction

function[img_ret]=cv_thresh_truncate(image)
    pyImport simple_thresholding
    img_ret=simple_thresholding.thresh_trunc(image)
endfunction

function[img_ret]=cv_thresh_tozero(image)
    pyImport simple_thresholding
    img_ret=simple_thresholding.thresh_tozero(image)
endfunction

function[img_ret]=cv_thresh_tozero_inverse(image)
    pyImport simple_thresholding
    img_ret=simple_thresholding.thresh_tozero_inv(image)
endfunction

function[image_ret]=cv_getRotation(image,center1,angle,scale)
    pyImport rotation2d
    image_ret=rotation2d.getRotation(image,center1,angle,scale)
endfunction

function[image_ret]=cv_blur(image,kSize)
    pyImport blur
    image_ret=blur.blur(image,kSize)
endfunction

function[image_ret]=cv_bilateralFilter(image,d,sigmaColor,sigmaSpace)
    pyImport bilateralFilter
    image_ret=bilateralFilter.bilateralfilter(image,kSize)
endfunction


function[image_ret]=cv_clahe(image,dclipLimit,titleGridSize)
    pyImport clahe
    image_ret=clahe.clahe(image,kSize)
endfunction

function[image_ret]=histogram2d(image,dclipLimit,titleGridSize)
    pyImport histogram_opencv
    image_ret=histogram_opencv.histogram2d(image,kSize)
endfunction

function[image_ret]=laplacian(image)
    pyImport imageGradients
    image_ret=imageGradients.laplacian(image)
endfunction

function[image_ret]=sobel(img, ddepth, xorder, yorder, ksize)
    pyImport imageGradients
    image_ret=sobel(img, ddepth, xorder, yorder, ksize)
endfunction





















