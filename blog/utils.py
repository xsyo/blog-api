import os



def img_upload_function(instance, filename):
    '''Возвращяет название загруженого файла'''

    file_type = filename.split('.')[-1]
    new_filename = f'{instance.id}.{file_type}'
    return os.path.join('media/', new_filename)


def heading_img_upload(instance, filename):
    '''Возвращяет название загруженого файла для рубрики поста'''

    file_type = filename.split('.')[-1]
    new_filename = f'{instance.name}.{file_type}'
    return os.path.join('media/heading/', new_filename)    

