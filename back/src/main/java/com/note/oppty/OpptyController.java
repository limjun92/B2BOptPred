package com.note.oppty;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;



@RestController
@RequestMapping("/oppty")
public class OpptyController {
	
	@Autowired
	private OpptyService OpptyService;
	
//	@GetMapping("/get")
//	public ResponseEntity<?> getUser() {
//		List<UserVo> users = User.selectUserList();
//		return ResponseEntity.status(HttpStatus.OK).body(users);
//	}
	
	//회원가입
	@PostMapping("/getData")
	public ResponseEntity<?> userEnroll(@RequestBody OpptyVo opptyVo) {
		System.out.println(opptyVo);
		String num = OpptyService.getData(opptyVo);
		return ResponseEntity.status(HttpStatus.OK).body(num);
	}
}
