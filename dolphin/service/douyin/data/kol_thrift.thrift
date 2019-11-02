
typedef string Json


service KolServer {
    string ping();
    Json fetch_sig_and_dytk(1: string uid);
    string checkout_user_agent();
}