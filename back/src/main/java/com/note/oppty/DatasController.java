package com.note.oppty;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.note.user.UserVo;

@RestController
@RequestMapping("/oppty")
public class DatasController {
	
	@Autowired
	private DatasService DatasService;
	
	@PostMapping("/insertData")
	public ResponseEntity<?> insertData(@RequestBody DatasVo datas) {
		System.out.println("=================================================================");
		System.out.println(datas);
		DatasService.insertDatas(datas);
		return ResponseEntity.status(HttpStatus.OK).body(1);
	}
	
	@GetMapping("/loadAllData")
	public ResponseEntity<?> loadAllData() {
		List<DatasVo> datas = DatasService.loadAllData();
		return ResponseEntity.status(HttpStatus.OK).body(datas);
	}
}
