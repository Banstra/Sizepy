import cv2

#image = cv2.imread('0')

cap=cv2.VideoCapture(0)
while True:
    ret, image =cap.read()
    cv2.imshow('webcam',image)
    k=cv2.waitKey(10)
    #
    # Gray, blur, adaptive threshold
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2_imshow(gray)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    # cv2_imshow(blur)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # cv2_imshow(thresh)

    # Morphological transformations
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    # cv2_imshow(opening)
    # Find contours
    cnts = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    for c in cnts:
        # Find perimeter of contour
        perimeter = cv2.arcLength(c, True)
        # Perform contour approximation
        approx = cv2.approxPolyDP(c, 0.04 * perimeter, True)
        # print(approx)
        # We assume that if the contour has more than a certain
        # number of verticies, we can make the assumption
        # that the contour shape is a circle
        if len(approx) > 3:
            # Obtain bounding rectangle to get measurements
            x, y, w, h = cv2.boundingRect(c)

            # Find measurements
            diameter = w
            radius = w / 2

            # Find centroid
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            # print(cX,cY)
            # Draw the contour and center of the shape on the image
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 4)
            cv2.drawContours(image, [c], 0, (36, 255, 12), 4)
            cv2.circle(image, (cX, cY), 5, (320, 159, 22), -1)

            # Draw line and diameter information
            cv2.line(image, (x, y + int(h / 2)), (x + w, y + int(h / 2)), (156, 188, 24), 3)
            cv2.putText(image, "Diameter: {}".format(diameter), (cX - 150, cY - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (156, 188, 24), 1)

    cv2.imwrite('image.png', image)
    cv2.imshow('image.png', image)
    cv2.imwrite('thresh.png', thresh)
    # cv2_imshow(thresh)
    cv2.imwrite('opening.png', opening)
    # cv2_imshow(opening)

   # image = cv2.imread('disk1.png')

    # Gray, blur, adaptive threshold
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2_imshow(gray)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    # cv2_imshow(blur)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # cv2_imshow(thresh)

    # Morphological transformations
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    # cv2_imshow(opening)
    # Find contours
    cnts = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    for c in cnts:
        # Find perimeter of contour
        perimeter = cv2.arcLength(c, True)
        # Perform contour approximation
        approx = cv2.approxPolyDP(c, 0.04 * perimeter, True)
        # print(approx)
        # We assume that if the contour has more than a certain
        # number of verticies, we can make the assumption
        # that the contour shape is a circle
        if len(approx) > 3:
            # Obtain bounding rectangle to get measurements
            x, y, w, h = cv2.boundingRect(c)

            # Find measurements
            diameter = w
            radius = w / 2

            # Find centroid
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            # print(cX,cY)
            # Draw the contour and center of the shape on the image
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 4)
            cv2.drawContours(image, [c], 0, (36, 255, 12), 4)
            cv2.circle(image, (cX, cY), 5, (320, 159, 22), -1)

            # Draw line and diameter information
            cv2.line(image, (x, y + int(h / 2)), (x + w, y + int(h / 2)), (156, 188, 24), 3)
            cv2.putText(image, "Diameter: {}".format(diameter), (cX - 150, cY - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (156, 188, 24), 1)

    cv2.imwrite('image.png', image)
    cv2.imshow('image.png', image)
    cv2.imwrite('thresh.png', thresh)
    # cv2_imshow(thresh)
    cv2.imwrite('opening.png', opening)
    # cv2_imshow(opening)

    #
    if k==27:
        break;
cap.release()
cv2.destroyAllWindows()


