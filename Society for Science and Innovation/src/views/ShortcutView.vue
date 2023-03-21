<template>
	<div class="shortcut-box">
		
		<section class="section">
			<!--<h2 class="section-title">
				<span>喜捷径</span>
			</h2>-->
			<div class="header">
				<span>
					<h2>桂林电子科技大学北海校区科学技术创新协会</h2>
					<h6>在这里你可以了解各种快捷操作，我们会帮助你快速定位所需的产品。如果你喜欢觉得我们帮助到了你，还希望你给与我们支持！</h6>
				</span>
				
			</div>
			<ul class="services">
				<li class="services__item" v-for="item in list" :key="item.id">
					<h3>{{item.title}}</h3>
					<p>{{item.content}}</p>
				</li>
			
			</ul>
		</section>
	
	</div>
</template>

<script>
export default {
	data(){
		return{
			list:[
				{id:1,title:'红林叶',content:'一个知你所不知，解你不能解之惑的微信公众号'},
				{id:2,title:'a-jingchao',content:'一个乐于在gitee分享优良开源项目的00后新时代程序猿'},
				{id:3,title:'魔法诗',content:'一个基于VUE3开发的仅包含前端的网页。炫酷，实用，开源将成为它的代名词'},
				{id:4,title:'Aubuary',content:'Github全球最大的同性交流平台分享开源项目的新成员'},
				{id:5,title:'XXXXXXXX',content:'jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj'},
				{id:6,title:'京茶吉鹿',content:'专注于写好每一行代码的coder，用键盘写诗的码农，追求每一个极致的开源项目的程序员'},
			
			]
		}
	}
	
}
</script>

<style scoped lang="scss">

// MIXINS
@mixin bp-sm { @media (min-width: 40.625em) { @content; } }
@mixin bp-md { @media (min-width: 48em)     { @content; } }
@mixin bp-lg { @media (min-width: 62em)     { @content; } }

@mixin pseudo-starter {
	content: '';
	display: block;
}

.shortcut-box {
	// 喜捷径描述
	--description:'在这里你可以了解各种快捷操作，我们会帮助你快速定位所需的产品。如果你喜欢觉得我们帮助到了你，还希望你给与我们支持！';
	// 页面颜色
	--color-brand-primary: hsl(var(--color-brand-primary-h), 43%, 43%);
	--color-brand-primary-h: 251;
	--color-brand-primary-s: 43%;
	--color-brand-primary-l: 43%;
	--color-brand-accent: hsl(var(--color-brand-accent-h), 96%, 61%);
	--color-brand-accent-h: 16;
	--color-brand-accent-s: 96%;
	--color-brand-accent-l: 61%;
	--color-brand-accent-bg: hsl(calc(var(--color-brand-accent-h) + 17), 100%, 96%);
	
	// 页面排列（排版）
	--ratio: 1.4; // The ratio number
	--s-6: calc(var(--s-5) / var(--ratio));
	--s-5: calc(var(--s-4) / var(--ratio));
	--s-4: calc(var(--s-3) / var(--ratio));
	--s-3: calc(var(--s-2) / var(--ratio));
	--s-2: calc(var(--s-1) / var(--ratio));
	--s-1:  calc(var(--s0) / var(--ratio));
	/*--s0: calc(1.05rem + 0.333vw);
	@include bp-sm {--s0: calc(1.25rem + 0.333vw); }
	@include bp-md {--s0:  calc(1.4rem + 0.333vw); }
	@include bp-lg {--s0:  calc(1.6rem + 0.333vw); }*/
	--s0: calc(1.05rem + 0.333vw);
	@include bp-sm {--s0: calc(1.25rem + 0.333vw); }
	@include bp-md {--s0:  calc(1.4rem + 0.333vw); }
	@include bp-lg {--s0:  calc(0.9rem + 0.333vw); }
	--s1: calc(var(--s0) * var(--ratio));
	--s2: calc(var(--s1) * var(--ratio));
	--s3: calc(var(--s2) * var(--ratio));
	--s4: calc(var(--s3) * var(--ratio));
	--s5: calc(var(--s4) * var(--ratio));
	--s6: calc(var(--s5) * var(--ratio));
	//font-size: 62.5%;  // ~10px
	line-height: 1.6;
	box-sizing: border-box;
	
	background-color: rgba(16 18 27 / 10%);
	overflow-x: hidden;
}


.section {
	//padding: 0 var(--s3);
	padding: 20px 40px;
	
	
	.header{
		height: 330px;
		color: black;
		display: flex;
		flex-wrap: wrap;
		//background-color: #503F9DFF;
		z-index: -1;
		background-attachment: fixed;
		background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='487' height='243.5' viewBox='''");
		
		
		span{
			display: flex;
			flex-direction: column;
			width: 70%;
			
			
			h2{
				font-size: 2.5rem;
				font-weight: 500;
				margin: 0;
			}
			h6{
				font-size: 1rem;
				font-weight: 350;
				margin: 14px 0 0;
			}
			//background-color: green;
		}
		
		svg{
			margin: auto 0 auto 70px;
			width: 30%;
		}
	}
}


h2, h3, p, ul { margin: 0; }

ul {
	padding: 0;
	
	li {
		list-style-type: none;
		
		&:before {
			content: "\200B"; /* 添加任意空间 */
			clip: rect(0 0 0 0);
			height: 1px;
			width: 1px;
			position: absolute;
		}
	}
}


.services {
	@include bp-sm {
		grid-template-columns: repeat(7, 1fr);
		grid-template-rows: minmax(100px, 1fr);
	}
	
	display: grid;
	grid-gap: var(--s2);
	margin: 0 calc(var(--s3) * -1);
	padding: var(--s6) var(--s3);
	@include bp-sm {padding: 0 var(--s3); }
	position: relative;
	z-index: 1;
	
	
	
	&:before {
		@include pseudo-starter;
		position: absolute;
		top: 0;
		left: 0;
		//background: var(--color-brand-accent-bg);
		background-color: rgba(16 18 27 / 20%);
		width: 100%;
		height: 100%;
		transform: skew(0deg, 10deg);
		background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='487' height='243.5' viewBox='");
	}
	
	&__item {
		background: #fff;
		padding: calc(var(--s2) - 0.6rem) var(--s1);
		border-radius: 25px;
		box-shadow: 0 7px 20px rgba(100, 28, 2, 0.135);
		@include bp-sm { transform: translateY(-85px); }
		@include bp-md { transform: translateY(-130px); }
		transition: all 300ms ease, transform 300ms cubic-bezier(0.175, 0.885, 0.32, 1.275);
		position: relative;
		z-index: 1;
		
		&:nth-of-type(1) {
			@include bp-sm { grid-column: 1 / -1; grid-row: 4 }
			
			@include bp-lg {
				grid-column: 5 / -1;
				grid-row: 3; }
		}
		
		&:nth-of-type(2) {
			@include bp-sm {
				grid-column: 1 / span 3;
				grid-row: 2;
			}
			
			@include bp-lg {
				grid-column: 3 / span 2;
				grid-row: auto;
			}
		}
		
		&:nth-of-type(3) {
			@include bp-sm { grid-column: 4 / -1; }
			
			@include bp-lg {
				grid-column: 4 / -1;
				grid-row: 2;
			}
		}
		
		&:nth-of-type(4) {
			@include bp-sm { grid-column: 1 / span 4; }
			
			@include bp-lg { grid-column: 1 / span 3; }
		}
		
		&:nth-of-type(5) {
			@include bp-sm { grid-column: 5 / -1; }
			
			@include bp-lg { grid-column: 1 / span 4; }
		}
		
		&:nth-of-type(6) {
			@include bp-sm { grid-column: 1 / span 4; grid-row: 1 }
			
			@include bp-lg {
				grid-column: 1 / span 2;
				grid-row: 1;
			}
		}
		
		h3 {
			color: var(--color-brand-primary);
			font-size: var(--s1);
			line-height: 1.2;
		}
		
		&:after {
			@include pseudo-starter;
			position: absolute;
			bottom: 0;
			right: 0;
			width: 50px;
			height: 50px;
			border-radius: 25px 0;
			cursor: pointer;
			transition: inherit;
			background-color: var(--color-brand-accent);
			background-size: 20px 20px;
			background-repeat: no-repeat;
			background-position: center;
			//链接icon
			background-image: url("data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9JzMwMHB4JyB3aWR0aD0nMzAwcHgnICBmaWxsPSIjZmZmZmZmIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGRhdGEtbmFtZT0iTGF5ZXIgMSIgdmlld0JveD0iMCAwIDEwMCAxMDAiIHg9IjBweCIgeT0iMHB4Ij48dGl0bGU+NTI8L3RpdGxlPjxwYXRoIGQ9Ik04MS4zMDMyOSwzOC41MjkzOUExNC4wMTgsMTQuMDE4LDAsMSwwLDYxLjQ3NywxOC43MDY3MUw0Ny4wMDMxNSwzMy4xNzkxNGExNC4wMzAzNywxNC4wMzAzNywwLDAsMCwwLDE5LjgyMTcxLDQuODAxMTMsNC44MDExMywwLDAsMS02Ljc4OTc5LDYuNzg5ODcsMjMuNjQzMjcsMjMuNjQzMjcsMCwwLDEsMC0zMy40MDE0NUw1NC42ODcyMSwxMS45MTY4NEEyMy42MjAzLDIzLjYyMDMsMCwwLDEsODguMDkzMDgsNDUuMzE5MjdMODAuOTIzOCw1Mi40ODcxMWE0LjgwMTE0LDQuODAxMTQsMCwwLDEtNi43ODk4LTYuNzg5ODdaTTExLjkwNzQxLDg4LjA5MzlhMjMuNjUwNTMsMjMuNjUwNTMsMCwwLDAsMzMuNDA1ODYtLjAwMUw1OS43ODY2NCw3My42MjE0N2EyMy42MTU4MywyMy42MTU4MywwLDAsMCwwLTMzLjQwMTQ1LDQuODAxMTQsNC44MDExNCwwLDAsMC02Ljc4OTc5LDYuNzg5ODgsMTQuMDE1MzEsMTQuMDE1MzEsMCwwLDEsMCwxOS44MjI2OEwzOC41MjM0OCw4MS4zMDRBMTQuMDE4LDE0LjAxOCwwLDEsMSwxOC42OTcyLDYxLjQ4MTM1TDI1Ljg2Niw1NC4zMTM1YTQuODAxMTQsNC44MDExNCwwLDAsMC02Ljc4OTgtNi43ODk4N2wtNy4xNjg3OSw3LjE2Nzg1QTIzLjY0NDg5LDIzLjY0NDg5LDAsMCwwLDExLjkwNzQxLDg4LjA5MzlaIj48L3BhdGg+PC9zdmc+");
		}
		
		p {
			margin-top: var(--s-1);
			font-weight: 400;
			color: hsl(250deg, 7%, 46%);
		}
		
		&:hover {
			@include bp-sm { transform: translateY(-93px);  }
			@include bp-md { transform: translateY(-138px); }
			background-color: var(--color-brand-accent);
			
			h3 { color: #fff; }
			
			p  { color: hsla(0, 0%, 100%, .8); }
			
			&:after {
				background-color: #fff;
				background-image: url("data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9JzMwMHB4JyB3aWR0aD0nMzAwcHgnICBmaWxsPSIjZmI2ZjNjIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGRhdGEtbmFtZT0iTGF5ZXIgMSIgdmlld0JveD0iMCAwIDEwMCAxMDAiIHg9IjBweCIgeT0iMHB4Ij48dGl0bGU+NTI8L3RpdGxlPjxwYXRoIGQ9Ik04MS4zMDMyOSwzOC41MjkzOUExNC4wMTgsMTQuMDE4LDAsMSwwLDYxLjQ3NywxOC43MDY3MUw0Ny4wMDMxNSwzMy4xNzkxNGExNC4wMzAzNywxNC4wMzAzNywwLDAsMCwwLDE5LjgyMTcxLDQuODAxMTMsNC44MDExMywwLDAsMS02Ljc4OTc5LDYuNzg5ODcsMjMuNjQzMjcsMjMuNjQzMjcsMCwwLDEsMC0zMy40MDE0NUw1NC42ODcyMSwxMS45MTY4NEEyMy42MjAzLDIzLjYyMDMsMCwwLDEsODguMDkzMDgsNDUuMzE5MjdMODAuOTIzOCw1Mi40ODcxMWE0LjgwMTE0LDQuODAxMTQsMCwwLDEtNi43ODk4LTYuNzg5ODdaTTExLjkwNzQxLDg4LjA5MzlhMjMuNjUwNTMsMjMuNjUwNTMsMCwwLDAsMzMuNDA1ODYtLjAwMUw1OS43ODY2NCw3My42MjE0N2EyMy42MTU4MywyMy42MTU4MywwLDAsMCwwLTMzLjQwMTQ1LDQuODAxMTQsNC44MDExNCwwLDAsMC02Ljc4OTc5LDYuNzg5ODgsMTQuMDE1MzEsMTQuMDE1MzEsMCwwLDEsMCwxOS44MjI2OEwzOC41MjM0OCw4MS4zMDRBMTQuMDE4LDE0LjAxOCwwLDEsMSwxOC42OTcyLDYxLjQ4MTM1TDI1Ljg2Niw1NC4zMTM1YTQuODAxMTQsNC44MDExNCwwLDAsMC02Ljc4OTgtNi43ODk4N2wtNy4xNjg3OSw3LjE2Nzg1QTIzLjY0NDg5LDIzLjY0NDg5LDAsMCwwLDExLjkwNzQxLDg4LjA5MzlaIj48L3BhdGg+PC9zdmc+");
			}
		}
	}
}

</style>