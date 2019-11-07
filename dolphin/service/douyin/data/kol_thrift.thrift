
typedef string Json


service KolServer {
    string ping();
    Json fetch_sig_and_dytk(1: string uid, 2: optional string dytk, 3: optional string tac);
    string checkout_user_agent();
}