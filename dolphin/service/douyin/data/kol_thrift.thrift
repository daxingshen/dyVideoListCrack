
typedef string Json


service KolServer {
    string ping();
    Json fetch_all_works(1: string uid);
    Json fetch_sig_and_dytk(1: string uid);
    string checkout_user_agent();
}