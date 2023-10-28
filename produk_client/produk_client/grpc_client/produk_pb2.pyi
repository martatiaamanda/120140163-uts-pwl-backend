from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Produk(_message.Message):
    __slots__ = ["id", "nama", "deskripsi", "harga", "gambar", "stok"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAMA_FIELD_NUMBER: _ClassVar[int]
    DESKRIPSI_FIELD_NUMBER: _ClassVar[int]
    HARGA_FIELD_NUMBER: _ClassVar[int]
    GAMBAR_FIELD_NUMBER: _ClassVar[int]
    STOK_FIELD_NUMBER: _ClassVar[int]
    id: int
    nama: str
    deskripsi: str
    harga: float
    gambar: str
    stok: int
    def __init__(self, id: _Optional[int] = ..., nama: _Optional[str] = ..., deskripsi: _Optional[str] = ..., harga: _Optional[float] = ..., gambar: _Optional[str] = ..., stok: _Optional[int] = ...) -> None: ...

class ProdukListRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ProdukRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ProdukResponse(_message.Message):
    __slots__ = ["id", "nama", "deskripsi", "harga", "gambar", "stok"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAMA_FIELD_NUMBER: _ClassVar[int]
    DESKRIPSI_FIELD_NUMBER: _ClassVar[int]
    HARGA_FIELD_NUMBER: _ClassVar[int]
    GAMBAR_FIELD_NUMBER: _ClassVar[int]
    STOK_FIELD_NUMBER: _ClassVar[int]
    id: int
    nama: str
    deskripsi: str
    harga: float
    gambar: str
    stok: int
    def __init__(self, id: _Optional[int] = ..., nama: _Optional[str] = ..., deskripsi: _Optional[str] = ..., harga: _Optional[float] = ..., gambar: _Optional[str] = ..., stok: _Optional[int] = ...) -> None: ...

class ProdukListResponse(_message.Message):
    __slots__ = ["produk"]
    PRODUK_FIELD_NUMBER: _ClassVar[int]
    produk: _containers.RepeatedCompositeFieldContainer[Produk]
    def __init__(self, produk: _Optional[_Iterable[_Union[Produk, _Mapping]]] = ...) -> None: ...

class ProdukCreateRequest(_message.Message):
    __slots__ = ["nama", "deskripsi", "harga", "gambar", "stok"]
    NAMA_FIELD_NUMBER: _ClassVar[int]
    DESKRIPSI_FIELD_NUMBER: _ClassVar[int]
    HARGA_FIELD_NUMBER: _ClassVar[int]
    GAMBAR_FIELD_NUMBER: _ClassVar[int]
    STOK_FIELD_NUMBER: _ClassVar[int]
    nama: str
    deskripsi: str
    harga: float
    gambar: str
    stok: int
    def __init__(self, nama: _Optional[str] = ..., deskripsi: _Optional[str] = ..., harga: _Optional[float] = ..., gambar: _Optional[str] = ..., stok: _Optional[int] = ...) -> None: ...

class ProdukCreateResponse(_message.Message):
    __slots__ = ["id", "nama", "deskripsi", "harga", "gambar", "stok"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAMA_FIELD_NUMBER: _ClassVar[int]
    DESKRIPSI_FIELD_NUMBER: _ClassVar[int]
    HARGA_FIELD_NUMBER: _ClassVar[int]
    GAMBAR_FIELD_NUMBER: _ClassVar[int]
    STOK_FIELD_NUMBER: _ClassVar[int]
    id: int
    nama: str
    deskripsi: str
    harga: float
    gambar: str
    stok: int
    def __init__(self, id: _Optional[int] = ..., nama: _Optional[str] = ..., deskripsi: _Optional[str] = ..., harga: _Optional[float] = ..., gambar: _Optional[str] = ..., stok: _Optional[int] = ...) -> None: ...

class ProdukUpdateRequest(_message.Message):
    __slots__ = ["id", "nama", "deskripsi", "harga", "gambar", "stok"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAMA_FIELD_NUMBER: _ClassVar[int]
    DESKRIPSI_FIELD_NUMBER: _ClassVar[int]
    HARGA_FIELD_NUMBER: _ClassVar[int]
    GAMBAR_FIELD_NUMBER: _ClassVar[int]
    STOK_FIELD_NUMBER: _ClassVar[int]
    id: int
    nama: str
    deskripsi: str
    harga: float
    gambar: str
    stok: int
    def __init__(self, id: _Optional[int] = ..., nama: _Optional[str] = ..., deskripsi: _Optional[str] = ..., harga: _Optional[float] = ..., gambar: _Optional[str] = ..., stok: _Optional[int] = ...) -> None: ...

class ProdukUpdateResponse(_message.Message):
    __slots__ = ["id", "nama", "deskripsi", "harga", "gambar", "stok"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAMA_FIELD_NUMBER: _ClassVar[int]
    DESKRIPSI_FIELD_NUMBER: _ClassVar[int]
    HARGA_FIELD_NUMBER: _ClassVar[int]
    GAMBAR_FIELD_NUMBER: _ClassVar[int]
    STOK_FIELD_NUMBER: _ClassVar[int]
    id: int
    nama: str
    deskripsi: str
    harga: float
    gambar: str
    stok: int
    def __init__(self, id: _Optional[int] = ..., nama: _Optional[str] = ..., deskripsi: _Optional[str] = ..., harga: _Optional[float] = ..., gambar: _Optional[str] = ..., stok: _Optional[int] = ...) -> None: ...

class ProdukDeleteRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ProdukDeleteResponse(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class HitungHargaRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[_Iterable[int]] = ...) -> None: ...

class HitungHargaResponse(_message.Message):
    __slots__ = ["harga"]
    HARGA_FIELD_NUMBER: _ClassVar[int]
    harga: float
    def __init__(self, harga: _Optional[float] = ...) -> None: ...
