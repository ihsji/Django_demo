def response_data(status_code=0, message=None, data={}, **kwargs):
    return dict({
        'status_code': status_code,
        'message': message,
        'data': data
        }, **kwargs
    )

class MovieError():
    MovieNotFound = (10001, '电影信息不存在')
    # 其他电影相关的错误信息...

class UserError():
    UserNotFound = (20001, '用户信息不存在')
    CollectMovieFailed = (20002, '收藏失败')
    CancelMovieFailed = (20003, '取消收藏失败')
    NotCollectMovie = (20004, '未收藏该电影')
    # 其他用户相关的错误信息...


