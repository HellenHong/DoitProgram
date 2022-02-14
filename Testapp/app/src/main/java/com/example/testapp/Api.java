package com.example.testapp;

import retrofit2.Call;
import retrofit2.http.Field;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.POST;

public interface Api {

    //일단은 pdf만.. document.php 파일 역시 pdf위주
    @FormUrlEncoded
    @POST("upload_document.php")
    Call<FileResponse> uploadDocument(
            @Field("PDF") String encodedFile
    );

}