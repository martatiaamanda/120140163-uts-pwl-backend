from concurrent import futures
import logging
import grpc
import produk_pb2
import produk_pb2_grpc

from database.config import engine
from sqlalchemy import insert, select, update, delete, desc

from models.produk import Produk


class ProductsServicer(produk_pb2_grpc.ProdukServiceServicer):
    def FindById(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(
                    select(Produk).where(Produk.id == request.id)
                ).first()

                conn.commit()

            return produk_pb2.ProdukResponse(
                id=res[0],
                nama=res[1],
                harga=res[2],
                deskripsi=res[3],
                stok=res[4],
                gambar=res[5],
            )
        except Exception as e:
            return produk_pb2.ProdukResponse()

    def FindAll(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(select(Produk).order_by(desc(Produk.id))).all()

                listProduk = []

                for row in res:
                    listProduk.append(
                        produk_pb2.Produk(
                            id=row[0],
                            nama=row[1],
                            harga=row[2],
                            deskripsi=row[3],
                            stok=row[4],
                            gambar=row[5],
                        )
                    )

                conn.commit()

            return produk_pb2.ProdukListResponse(
                produk=listProduk,
            )
        except Exception as e:
            print(f"Error df {e}")
            return produk_pb2.ProdukListResponse()

    def Create(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(
                    insert(Produk).values(
                        nama=request.nama,
                        harga=request.harga,
                        deskripsi=request.deskripsi,
                        stok=request.stok,
                        gambar=request.gambar,
                    )
                )

                conn.commit()

            return produk_pb2.ProdukCreateResponse(
                nama=request.nama,
                harga=request.harga,
                deskripsi=request.deskripsi,
                stok=request.stok,
                gambar=request.gambar,
            )
        except Exception as e:
            print(f"Error {e}")
            return produk_pb2.ProdukCreateResponse()

    def Update(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(
                    update(Produk)
                    .where(Produk.id == request.id)
                    .values(
                        nama=request.nama,
                        harga=request.harga,
                        deskripsi=request.deskripsi,
                        stok=request.stok,
                        gambar=request.gambar,
                    )
                )

                conn.commit()

            return produk_pb2.ProdukUpdateResponse(
                id=request.id,
                nama=request.nama,
                harga=request.harga,
                deskripsi=request.deskripsi,
                stok=request.stok,
                gambar=request.gambar,
            )

        except Exception as e:
            print(f"Error as {e}")
            return produk_pb2.ProdukUpdateResponse()

    def Delete(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(delete(Produk).where(Produk.id == request.id))

                conn.commit()

            return produk_pb2.ProdukDeleteResponse(
                id=request.id,
            )

        except Exception as e:
            return produk_pb2.ProdukDeleteResponse()

    def HitungHarga(self, request, context):
        try:
            harga = 0

            ids = request.id

            for id in ids:
                with engine.connect() as conn:
                    conn.begin()

                    res = conn.execute(select(Produk).where(Produk.id == id)).first()

                    print(res)

                    if res is not None:
                        conn.execute(
                            update(Produk)
                            .where(Produk.id == id)
                            .values(stok=res[4] - 1)
                        )

                        harga += res[2]

                    conn.commit()

            return produk_pb2.HitungHargaResponse(
                harga=harga,
            )

        except Exception as e:
            return produk_pb2.HitungHargaResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    produk_pb2_grpc.add_ProdukServiceServicer_to_server(ProductsServicer(), server)
    server.add_insecure_port("localhost:7000")
    server.start()
    print("Server started at localhost:7000")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
