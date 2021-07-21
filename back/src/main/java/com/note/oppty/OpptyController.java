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
public class OpptyController {
	
	@Autowired
	private OpptyService OpptyService;
	
	@GetMapping("/getAll")
	public ResponseEntity<?> selectOpptyList() {
		List<OpptyVo> oppty = OpptyService.selectOpptyList();
		return ResponseEntity.status(HttpStatus.OK).body(oppty);
	}
	
	@PostMapping("/getData")
	public ResponseEntity<?> getData(@RequestBody OpptyVo opptyVo) {
		System.out.println(opptyVo);
		String num = OpptyService.getData(opptyVo);
		return ResponseEntity.status(HttpStatus.OK).body(num);
	}
}
