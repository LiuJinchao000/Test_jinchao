#include<iostream>

#include<opencv2/opencv.hpp>
#include <chrono>
#include <iostream>
class Timer
{    
private:
    std::chrono::time_point<std::chrono::high_resolution_clock> start,end;
    std::chrono::duration<double> duration;
public:
    Timer()
    {
        start=std::chrono::high_resolution_clock::now();
    }
    ~Timer()
    {
        end=std::chrono::high_resolution_clock::now();
        duration=end-start;
        double ms=duration.count()*1000.0;
        std::cout<<"Timer took : "<<ms<<std::endl;
    }
};
using namespace cv;

using namespace std;

void histogram_eq_demo(Mat &image)
{
    Mat gray;
    cvtColor(image, gray, COLOR_BGR2GRAY);
    //直方图均衡化只支持灰度图像，不支持彩色图像。
    imshow("灰度图像", gray);
    Mat dst;
    equalizeHist(gray, dst);
    imshow("直方图均衡化", dst);
}

int main()

{
    Timer a=Timer();
    Mat m4 = imread("../rabbit.jpg");

/* 
    int dims=m4.channels();
    int h=m4.rows;
    int w=m4.cols;
    for(int col=0;col<w;col++)
    {
        for(int row=0;row<h;row++)
        {
            Vec3f bgr = m4.at<float>(row,col);
            m4.at<Vec3f>(row,col)[0] =255-bgr[0];
            m4.at<Vec3f>(row,col)[1] =255-bgr[1];
            m4.at<Vec3f>(row,col)[2] =255-bgr[2];
            
        }

    } */
    histogram_eq_demo(m4);
    namedWindow("test",WINDOW_FREERATIO);
    imshow("test",m4);
    waitKey(5000);
    dnn::Net net = dnn::readNetFromTensorflow(root_dir+ "opencv_face_detector_uint8.pb", root_dir+"opencv_face_detector.pbtxt");
VideoCapture capture("D:/images/video/example_dsh.mp4");
Mat frame;
while (true) {
    capture.read(frame);
    if (frame.empty()) {
        break;
    }
    Mat blob = dnn::blobFromImage(frame, 1.0, Size(300, 300), Scalar(104, 177, 123), false, false);
    net.setInput(blob);// NCHW
    Mat probs = net.forward(); // 
    Mat detectionMat(probs.size[2], probs.size[3], CV_32F, probs.ptr<float>());
    // 解析结果
    for (int i = 0; i < detectionMat.rows; i++) {
        float confidence = detectionMat.at<float>(i, 2);
        if (confidence > 0.5) {
            int x1 = static_cast<int>(detectionMat.at<float>(i, 3)*frame.cols);
            int y1 = static_cast<int>(detectionMat.at<float>(i, 4)*frame.rows);
            int x2 = static_cast<int>(detectionMat.at<float>(i, 5)*frame.cols);
            int y2 = static_cast<int>(detectionMat.at<float>(i, 6)*frame.rows);
            Rect box(x1, y1, x2 - x1, y2 - y1);
            rectangle(frame, box, Scalar(0, 0, 255), 2, 8, 0);
        }
    }
    imshow("人脸检测演示", frame);
    int c = waitKey(1);
    if (c == 27) { // 退出
        break;
    }
}
    return 0;

}
