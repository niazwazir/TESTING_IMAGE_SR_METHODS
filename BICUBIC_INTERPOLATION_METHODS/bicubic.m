I = imread('baby_x2_GT.png');
Y = imresize(I,[160,256],'Method','bicubic');
figure;
imshow(Y);