package com.note.reader;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.Charset;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import com.note.user.UserVo;

@RestController
@RequestMapping("/file")
public class ReadController {
	
	@GetMapping("/read")
	public void getFile() throws IOException {
		List<List<String>> list = new ArrayList<List<String>>();
		FileInputStream input=new FileInputStream("C:\\Users\\limju\\OneDrive\\바탕 화면\\신입사원역량강화 프로젝트\\B2BOptPred\\oppty.csv");
		InputStreamReader reader=new InputStreamReader(input,"euc-kr");
        BufferedReader in=new BufferedReader(reader);
        
        String line = "";
        int cnt = 0;
        
        while((line=in.readLine()) != null) {
			String[] token = line.split(",");
			List<String> tempList = new ArrayList<String>(Arrays.asList(token));
			list.add(tempList);
			cnt++;
			if(cnt < 5) {
				System.out.println(tempList);
			}
		}
        System.out.println(list.size());
	}
	
	@PostMapping("/upload")
	public ResponseEntity<List<String>> uploadFile(MultipartFile files) throws IOException {
		List<List<String>> list = new ArrayList<List<String>>();
		System.out.println(files);
		System.out.println(files.getName());
		System.out.println(files.getSize());
		System.out.println(files.getResource());
		byte[] data = files.getBytes();
		System.out.println(data.length);
		for(int i = 0;i<5;i++) {
			System.out.println(data[i]);
		}
		System.out.println(files.toString());
		System.out.println(files.getOriginalFilename());
		File f = new File("C:\\Users\\limju\\Downloads\\" + files.getOriginalFilename() + "asd");
//		System.out.println(f.getPath());
		//files.transferTo(f);
		InputStreamReader reader=new InputStreamReader(files.getInputStream(),"euc-kr");
		BufferedReader in=new BufferedReader(reader);
        
        String line = "";
        int cnt = 0;
        
        while((line=in.readLine()) != null) {
			String[] token = line.split(",");
			List<String> tempList = new ArrayList<String>(Arrays.asList(token));
			list.add(tempList);
			cnt++;
			if(cnt < 5) {
				System.out.println(tempList);
			}
		}
        System.out.println(list.size());
        return ResponseEntity.status(HttpStatus.OK).body(list.get(0));
	}
}


