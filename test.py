import pyimgur

r = pyimgur.Imgur(
    client_id="ca8c45141727850",
    client_secret="6d286bf906a36e8763dc2d4acc525276b047944a"
)
r.get_image(id="eZ6CCG0").download(path="", name="test", overwrite=False, size=None)