def includeme(config):
    # config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route("home", "/")
    config.add_route("jumlah_harga", "/api/v1/produk/jumlah_harga")
    config.add_route("produk", "/api/v1/produk{action:.*}")
