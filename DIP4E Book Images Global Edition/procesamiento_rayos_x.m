img = imread('bonescan.tif');
subplot(241)
imshow(img,[])
title('Imagen Original');

filtro_laplace=[-1 -1 -1;-1 9 -1;-1 -1 -1];
laplaciano = uint8(conv2(img, filtro_laplace,'same'));
subplot(242)
imshow(laplaciano,[]);
title('realce bordes laplaciano');

[magnitudeImage, directionImage] = imgradient(img, 'Sobel');
sobel=uint8(magnitudeImage);
subplot(243)
imshow(sobel);
title('sobel de la imagen original');

filtro_media=ones(3,3)/9;
sobelSmooth = uint8(conv2(sobel, filtro_media,'same'));
subplot(244)
imshow(sobelSmooth);
title('sobel suavizado');

maskImage = immultiply (uint16(laplaciano), uint16(sobelSmooth));
mask = im2uint8(maskImage);
subplot(245)
imshow(mask,[]);
title('mascara laplaciano * sobel smooth');

img_enhanced = imadd(img,mask);
subplot(246)
imshow(img_enhanced,[]);
title('imagen original mejorada');

%power transformation
img_normalizada = double(img_enhanced) / 255;
img_transform_norm = img_normalizada.^0.5;
img_final = uint8(img_transform_norm * 255);
subplot(247)
imshow(img_final,[]);
title('imagen final');
