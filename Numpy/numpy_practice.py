{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy\n",
    "a = numpy.arange(27)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[ 0,  1,  2],\n",
       "        [ 3,  4,  5],\n",
       "        [ 6,  7,  8]],\n",
       "\n",
       "       [[ 9, 10, 11],\n",
       "        [12, 13, 14],\n",
       "        [15, 16, 17]],\n",
       "\n",
       "       [[18, 19, 20],\n",
       "        [21, 22, 23],\n",
       "        [24, 25, 26]]])"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.reshape(3,3,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "numpy.ndarray"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[187 158 104 121 143]\n",
      " [198 125 255 255 147]\n",
      " [209 134 255  97 182]]\n"
     ]
    }
   ],
   "source": [
    "im_g = cv2.imread(\"smallgray.png\",0)\n",
    "print(im_g)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cv2.imwrite(\"gray.png\",im_g)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3, 5)"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "im_g.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[104, 121],\n",
       "       [255, 255]], dtype=uint8)"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "im_g[0:2,2:4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[209, 134, 255,  97, 182]], dtype=uint8)"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "im_g[2:4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[187 198 209]\n",
      "[158 125 134]\n",
      "[104 255 255]\n",
      "[121 255  97]\n",
      "[143 147 182]\n"
     ]
    }
   ],
   "source": [
    "for i in im_g.T:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "187\n",
      "158\n",
      "104\n",
      "121\n",
      "143\n",
      "198\n",
      "125\n",
      "255\n",
      "255\n",
      "147\n",
      "209\n",
      "134\n",
      "255\n",
      "97\n",
      "182\n"
     ]
    }
   ],
   "source": [
    "for i in im_g.flat:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "ims = numpy.hstack((im_g,im_g))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[187 158 104 121 143 187 158 104 121 143]\n",
      " [198 125 255 255 147 198 125 255 255 147]\n",
      " [209 134 255  97 182 209 134 255  97 182]]\n"
     ]
    }
   ],
   "source": [
    "print(ims)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "img = numpy.vstack((im_g,im_g))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[187 158 104 121 143]\n",
      " [198 125 255 255 147]\n",
      " [209 134 255  97 182]\n",
      " [187 158 104 121 143]\n",
      " [198 125 255 255 147]\n",
      " [209 134 255  97 182]]\n"
     ]
    }
   ],
   "source": [
    "print(img)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "lst = numpy.vsplit(img,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[187, 158, 104, 121, 143],\n",
       "       [198, 125, 255, 255, 147]], dtype=uint8)"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lst[0]"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
